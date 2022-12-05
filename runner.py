#!/usr/bin/env python
import os
import time
import argparse
import filecmp
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent

class SessionHandler(FileSystemEventHandler):
    def __init__(self, base_dir, args):
        self.base_dir = base_dir
        self.session_dir = os.path.join(base_dir, str(args.day[0]))
        self.cache_dir = os.path.join(base_dir, '.runner_cache/')

        self.main_file = os.path.join(self.session_dir, 'main.cpp')
        self.input_file = os.path.join(self.session_dir, 'input.txt')
        self.exec_file = os.path.join(self.session_dir, 'main')

        self.cache_exec_file = os.path.join(self.cache_dir, 'exec')
        self.cache_main_file = os.path.join(self.cache_dir, 'main.cpp')
        self.cache_input_file = os.path.join(self.cache_dir, 'input.txt')

        self.args = args

    def config_is_valid(self):
        if os.path.exists(self.main_file):
            print(f'binded to main file at {self.main_file}')
        else:
            print(f'could not find main file at {self.main_file}')
            return False

        if self.args.autorun and os.path.exists(self.input_file):
            print(f'binded to input file at {self.input_file}')
        elif self.args.autorun and not os.path.exists(self.input_file):
            print(f'could not find input file at {self.input_file}')
            return False
        return True

    def on_modified(self, event):
        do_compile = False
        do_run = False

        if isinstance(event, FileModifiedEvent):
            filecmp.clear_cache()
            if event.src_path == self.main_file:
                # check if actually different
                # some reason we have double file-modified events with nvim??
                if not os.path.exists(self.cache_main_file):
                    no_change = False
                else:
                    no_change = filecmp.cmp(
                            self.main_file, self.cache_main_file, shallow=False)


                if no_change == False:
                    # update cached file
                    print(">> detected change in main.cpp")
                    os.system(f'cp {self.main_file} {self.cache_main_file}')
                    do_compile = True
                    do_run = self.args.autorun

            if event.src_path == self.input_file and self.args.autorun:
                if not os.path.exists(self.cache_input_file):
                    no_change = False
                else:
                    no_change = filecmp.cmp(
                            self.input_file, self.cache_input_file, shallow = False)

                if no_change == False:
                    # update cached file
                    print(">> detected change in input.txt")
                    os.system(f'cp {self.input_file} {self.cache_input_file}')
                    do_run = True

        # compile if needed
        if do_compile:
            print(">> compiling")
            if os.system(f'g++ -O2 -o {self.cache_exec_file} {self.main_file}') != 0:
                # error occured during compiling
                return
            else:
                os.system(f'mv {self.cache_exec_file} {self.exec_file}')

        if do_run:
            command = f'timeout {self.args.limit[0]}s {self.exec_file} < {self.input_file}'
            print(f">> running with time limit = {self.args.limit[0]}s")
            os.system(command)
            print("<< done!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Start auto compiling and running')
    parser.add_argument('day', type=int, nargs=1,
            help = 'the day to bind auto-runner to')
    parser.add_argument('-a', '--autorun', action='store_true',
            help = 'runs executable on build success or change of input.txt')
    parser.add_argument('-l', '--limit', nargs=1, type=int, default=[5],
            help = 'process time limit')
    parser.add_argument('-i', '--init', action='store_true',
            help = 'initializes folder for specified day')
    args = parser.parse_args()

    handler = SessionHandler(
        base_dir = os.path.dirname(os.path.realpath(__file__)),
        args = args,
    )

    # initialize folder

    if not handler.config_is_valid():
        exit()

    observer = Observer()
    observer.schedule(handler, handler.session_dir)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

