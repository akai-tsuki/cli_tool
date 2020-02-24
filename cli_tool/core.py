# -*- coding: utf-8 -*-

# from argparse import ArgumentParser
from sample01 import Sample01

# import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

def main():
    print('Start')
    sample = Sample01()
    text = sample.get_msg()
    print(text)
    print('End')

if __name__ == "__main__":
    main()