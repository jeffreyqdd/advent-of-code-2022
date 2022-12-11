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
        'cpp' : ['g++ --std=C++11 -O2 -o {exec_file} {src_file}', '{exec_file}'],
        'py'  : ['', '{src_file}']
}

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
            os.system(f'cp template/ {config.session_dir} -r')
        else:
            print(f'session at {config.session_dir} does not exist')
            print(f'\tplease pass in the -i flag to explicitly init session')
            exit()

    print(config.get_bindable_exec_files())
