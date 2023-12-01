#!/usr/bin/env python
import os
import time
import glob
import argparse
import filecmp
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent

"""language build rules. key=file extension, value=[build rules, exec file]
1. {exec_file} -> name of the compiled executable
2. {src_file} -> name of the source file

- leave build rule empty str if there is nothing to be done for build
"""
exec_rules = {
        'cpp' : ['g++ --std=c++11 -O2 -o {exec_file} {src_file}', '{exec_file}'],
        'py'  : ['', '{src_file}']
}

# input file name
input_file = 'input.txt'

class Config:
    def __init__(self, day_number, cache_dir='.runner_cache'):
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.session_dir = os.path.join(self.base_dir, str(day_number))
        self.cache_dir = os.path.join(self.base_dir, cache_dir)

    def get_bindable_exec_files(self):
        """returns all files extensions supported by exec rules under
        self.session_director"""
        source_files = []
        for file in glob.iglob(self.session_dir + '/**', recursive=True):
            for k in exec_rules.keys():
                if f'.{k}' in file:
                    source_files.append(file)
        return source_files

    def get_bindable_input_file(self):
        """returns all files extensions supported by exec rules under
        self.session_director"""
        ret = []
        for file in glob.iglob(self.session_dir + '/**', recursive=True):
            if input_file == file.split('/')[-1]:
                ret.append(file)
        return ret

class SessionHandler(FileSystemEventHandler):
    def __init__(self, config, args):
        self.config = config
        self.source_files = config.get_bindable_exec_files()
        self.input_file = config.get_bindable_input_file()
        self.args = args
        self._last_source_file_extension = None
        self._last_source_file = None
    def on_modified(self, event):
        if not isinstance(event, FileModifiedEvent):
            return
        do_run = False
        build_succeeded = True
        source_file_extension = event.src_path.split('.')[-1]
        src_path = event.src_path
        if src_path in self.source_files and self._register_change(src_path):
            # file changed so do build_task
            build_command = exec_rules[source_file_extension][0].format(
                exec_file = os.path.join(self.config.session_dir, "main"),
                src_file = src_path
            )
            os.system('clear')
            print('>> detected change in source file executing build task:')
            print(f'\t{build_command}')
            if build_command != '':
                build_succeeded = os.system(build_command) == 0
            do_run = True

        if src_path in self.input_file and self._register_change(src_path):
            print('>> detected change in input file')
            do_run = True

        if do_run and build_succeeded:
            if 'txt' in source_file_extension:
                if self._last_source_file_extension is None:
                    print(f'>> skipping execute since source is ambiguous')
                    return
                else:
                    source_file_extension = self._last_source_file_extension
                    src_path = self._last_source_file
            else:
                self._last_source_file_extension = source_file_extension
                self._last_source_file = src_path

            run_command = exec_rules[source_file_extension][1].format(
                exec_file = os.path.join(self.config.session_dir, "main"),
                src_file = src_path
            ) + '< ' + self.input_file[0]
            run_command = f'timeout {self.args.limit[0]}s ' + run_command
            os.system('clear')
            print(f'>> executing file with time limit {self.args.limit[0]}s')
            os.system(run_command)

    def _register_change(self, changed_file):
        # returns true if files has changed
        file_base = changed_file.split('/')[-1]
        cache_file_equivalent = os.path.join(self.config.cache_dir, file_base)
        if not os.path.exists(cache_file_equivalent):
            os.system(f'touch {cache_file_equivalent}')

        no_change = filecmp.cmp(cache_file_equivalent, changed_file, shallow=False)
        os.system(f'cp {changed_file} {cache_file_equivalent}')
        return not no_change

if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(
            description='sets up day and automatically runs program on save')
    parser.add_argument(
            'day', type=int, nargs=1, help = 'advent of code day number')
    parser.add_argument(
            '-l', '--limit', nargs=1, type=int, default=[5], help = 'set process time limit')
    parser.add_argument(
            '-i', '--init', action='store_true', help = 'inits day if directory does not exist')

    args = parser.parse_args()

    # check if folder exists. if doesn't terminate if -i flag is not passed
    config = Config(args.day[0])
    if not os.path.exists(config.session_dir):
        if args.init:
            print(f'creating session at {config.session_dir}')
            os.system(f'cp -r template/ {config.session_dir}')
        else:
            print(f'session at {config.session_dir} does not exist')
            print(f'\tplease pass in the -i flag to explicitly init session')
            exit()
    handler = SessionHandler(config, args)
    for file in handler.source_files:
        print(f'binded to file: {file}')
    if len(handler.input_file) == 1:
        print(f'binded to input: {handler.input_file[0]}')
    else:
        print('warning: no input files found')

    observer = Observer()
    observer.schedule(handler, handler.config.session_dir)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
