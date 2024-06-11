#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2024-06-10
Purpose: Generate Zalgo text
"""

import argparse
import random
import sys

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Generate Zalgo text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='str',
                        nargs='?',
                        help='Initial string to Zalgo-fy. If not provided, read from stdin')

    parser.add_argument('-a',
                        '--adds-per-char',
                        metavar='int',
                        type=int,
                        default=1,
                        help='Number of additions per character')

    parser.add_argument('-l',
                        '--char-limit',
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

    parser.add_argument('-o',
                        '--one-per-line',
                        action='store_true',
                        help='Output one Zalgo-fied string per line')

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

    if args.string:
        string = args.string
    else:
        string = sys.stdin.read()

    adds_per_char = args.adds_per_char
    char_limit = args.char_limit
    amount_wanted = args.amount
    one_per_line = args.one_per_line

    if char_limit != 0:
        adds_per_char = (char_limit - len(string)) // len(string)

    for i in range(amount_wanted):
        print(zalgo(string, adds_per_char), end='\n' if one_per_line else '\t')

        if not one_per_line and ((i + 1) % 4 == 0):
            print()

    if not one_per_line:
        print()

if __name__ == '__main__':
    main()
