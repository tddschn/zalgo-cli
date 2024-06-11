__version__ = "0.2.2"

import random

def zalgo(string, adds_per_char):
    """Take the given string and add <adds_per_char> unicode combining characters after each character."""
    result = ''

    for char in string:
        for _ in range(adds_per_char):
            rand_bytes = random.randint(0x300, 0x36f).to_bytes(2, 'big')
            char += rand_bytes.decode('utf-16be')
        result += char

    return result
