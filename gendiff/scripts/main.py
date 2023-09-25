#!/usr/bin/env python

import argparse
from gendiff import generate_diff

  
def main():
    parser = argparse.ArgumentParser(description=
                                    'Compares two configuration'
                                    'files and shows a difference.'
                                    )
    parser.add_argument('filename1', metavar='ferst_file')
    parser.add_argument('filename2', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.ferst_file, args.second_file))


if __name__ == '__main__':
    main()
