# -*- coding: utf-8 -*-

# from argparse import ArgumentParser
from sample01 import Sample01
import argparse

# import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


def getArg():
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

    arg_values = getArg()
    print('Check args ---')
    print(arg_values.arg1)
    print(arg_values.bar)
    print(arg_values.number)

    print('Start ---')

    if arg_values.number is not None:
        sample_value = arg_values.number
    else:
        sample_value = 1

    sample = Sample01()
    sample.start(sample_value)

    print('End ---')


if __name__ == "__main__":
    main()
