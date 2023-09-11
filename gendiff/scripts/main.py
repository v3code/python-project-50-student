#!/usr/bin/env python

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description=
                                    'Compares two configuration'
                                    'files and shows a difference.'
                                    )
    parser.add_argument('filename1', metavar='ferst_file')
    parser.add_argument('filename2', metavar='second_file')
    args = parser.parse_args()

    return args
  
def main():
    args = parse_args()
    filename1, filename2 = args.filename1, args.filename2
    print(filename1, filename2)


if __name__ == '__main__':
    main()
