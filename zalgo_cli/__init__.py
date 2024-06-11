__version__ = "0.3.1"

import random
from typing import Iterable, Optional

def zalgo(string: str, adds_per_char: int, codepoints_to_add: Optional[Iterable[int]] = None) -> str:
    """Take the given string and add <adds_per_char> unicode combining characters after each character.
    If codepoints_to_add is provided, use it instead of random values.
    """
    result = ''

    if codepoints_to_add:
        codepoints_iterator = iter(codepoints_to_add)

    for char in string:
        for _ in range(adds_per_char):
            if codepoints_to_add:
                try:
                    char += chr(next(codepoints_iterator))
                except StopIteration:
                    pass  # No more codepoints to add
            else:
                rand_bytes = random.randint(0x300, 0x36f).to_bytes(2, 'big')
                char += rand_bytes.decode('utf-16be')
        result += char

    return result
