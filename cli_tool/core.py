# -*- coding: utf-8 -*-

from cli_tool.sample01 import Sample01
import argparse

import os
import logging
import logging.config

# logging.getLogger('cli_tool').addHandler(logging.NullHandler())

logging_config_filename = 'logging.ini'

if os.path.isfile(logging_config_filename):
    logging.config.fileConfig(logging_config_filename)


def get_arg():
    parser = argparse.ArgumentParser(
        prog='sample_cli',
        add_help=True
    )

    parser.add_argument(
        '-a', '--arg1', default='default_arg', help='sample arg1')
    parser.add_argument('-b', '--bar', required=True,
                        help='This arg is required')
    parser.add_argument('-n', '--number', type=int, help='put number')

    args = parser.parse_args()

    return args


def main():

    arg_values = get_arg()
    print('Check args ---')
    print(arg_values.arg1)
    print(arg_values.bar)
    print(arg_values.number)

    print('Start ---')
    print("name:" + __name__)

    if arg_values.number is not None:
        sample_value = arg_values.number
    else:
        sample_value = 1

    sample = Sample01()
    sample.start(sample_value)

    print('End ---')


if __name__ == "__main__":
    main()
