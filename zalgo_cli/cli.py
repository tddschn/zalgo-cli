#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2024-06-10
Purpose: Generate Zalgo text
"""

import argparse
import sys
import logging
from zalgo_cli import __version__, zalgo, strip_accents as dezalgo

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Generate or De-Zalgo text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='str',
                        nargs='?',
                        help='Initial string to Zalgo-fy or De-Zalgo-fy. If not provided, read from stdin')

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

    parser.add_argument('-o', '-1',
                        '--one-per-line',
                        action='store_true',
                        help='Output one Zalgo-fied string per line')

    parser.add_argument('-c',
                        '--codepoints',
                        metavar='str',
                        type=str,
                        default='',
                        help="Codepoints to Add (space-separated hex values, e.g., '0x036D 0x0368')")

    parser.add_argument('-d',
                        '--debug',
                        action='store_true',
                        help='Enable debug logging')

    parser.add_argument('-z',
                        '--dezalgo',
                        action='store_true',
                        help='De-Zalgo-fy the input string')

    parser.add_argument(
        '-V', '--version',
        action='version',
        version=f'%(prog)s {__version__}',
    )
    return parser.parse_args()

def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    if args.string:
        string = args.string
    else:
        string = sys.stdin.read()

    if args.dezalgo:
        print(dezalgo(string))
        return

    adds_per_char = args.adds_per_char
    char_limit = args.char_limit
    amount_wanted = args.amount
    one_per_line = args.one_per_line
    codepoints_to_add = [int(cp, 16) for cp in args.codepoints.strip().split()] if args.codepoints else None

    if args.debug and codepoints_to_add:
        logging.debug(f"Codepoints to add: {codepoints_to_add}")

    if char_limit != 0:
        adds_per_char = (char_limit - len(string)) // len(string)

    for i in range(amount_wanted):
        print(zalgo(string, adds_per_char, codepoints_to_add, args.debug), end='\n' if one_per_line else '\t')

        if not one_per_line and ((i + 1) % 4 == 0):
            print()

    if not one_per_line:
        print()

if __name__ == '__main__':
    main()
