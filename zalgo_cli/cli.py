#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2024-06-10
Purpose: Why not?
"""

import argparse
from pathlib import Path
import random

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Generate Zalgo text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='str',
                        help='Initial string to Zalgo-fy')

    parser.add_argument('-a',
                        '--adds_per_char',
                        metavar='int',
                        type=int,
                        default=1,
                        help='Number of additions per character')

    parser.add_argument('-l',
                        '--char_limit',
                        metavar='int',
                        type=int,
                        default=0,
                        help='Character limit [0 for no limit]')

    parser.add_argument('-n',
                        '--amount',
                        metavar='int',
                        type=int,
                        default=1,
                        help='Amount of Zalgo text to generate')

    return parser.parse_args()

def zalgo(string, adds_per_char):
    """Take the given string and add <adds_per_char> unicode combining characters after each character."""
    result = ''

    for char in string:
        for _ in range(adds_per_char):
            rand_bytes = random.randint(0x300, 0x36f).to_bytes(2, 'big')
            char += rand_bytes.decode('utf-16be')
        result += char

    return result

def main():
    """Make a jazz noise here"""

    args = get_args()

    string = args.string
    adds_per_char = args.adds_per_char
    char_limit = args.char_limit
    amount_wanted = args.amount

    if char_limit != 0:
        adds_per_char = (char_limit - len(string)) // len(string)

    for i in range(amount_wanted):
        print(zalgo(string, adds_per_char), end='')

        if ((i + 1) % 4 == 0):
            print()
        else:
            print('\t', end='')

    print()

if __name__ == '__main__':
    main()
