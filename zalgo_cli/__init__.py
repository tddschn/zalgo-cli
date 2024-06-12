__version__ = "0.4.0"

import random
from typing import Iterable, Optional
import logging

def codepoint_to_utf_char(codepoint: int) -> str:
    """Convert the given codepoint to a UTF-8 character."""
    # to bytes then decode to utf 16 be
    return codepoint.to_bytes(2, 'big').decode('utf-16be')

def zalgo(string: str, adds_per_char: int, codepoints_to_add: Optional[Iterable[int]] = None, debug: bool = False) -> str:
    """Take the given string and add <adds_per_char> unicode combining characters after each character.
    If codepoints_to_add is provided, use it instead of random values.
    """
    result = ''

    if codepoints_to_add:
        codepoints_iterator = iter(codepoints_to_add)

    for char in string:
        orig_char = char
        codepoint = None
        if codepoints_to_add:
            try:
                codepoint = next(codepoints_iterator)
            except StopIteration:
                codepoint = None
        
        for _ in range(adds_per_char):
            if codepoint:
                char += codepoint_to_utf_char(codepoint)
                if debug:
                    logging.debug(f"Added codepoint: U+{codepoint:04X} to {orig_char} -> {char}")
            else:
                random_codepoint = random.randint(0x300, 0x36f)
                char += codepoint_to_utf_char(random_codepoint)
                if debug:
                    logging.debug(f"Added codepoint: U+{random_codepoint:04X} to {orig_char} -> {char}")
        result += char
    
    return result
