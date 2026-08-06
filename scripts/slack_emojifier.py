#/// script
# requires-python = ">=3.14"
#///
from enum import auto, StrEnum

class LetterColor(StrEnum):
    YELLOW = "yellow"
    WHITE = "white"
    
    def invert(self) -> "LetterColor":
        if self == LetterColor.YELLOW:
            return LetterColor.WHITE
        else:
            return LetterColor.YELLOW

class Emojifier(object):

    PUNC_LOOKUP = {
        "@": "at",
        "#": "hash",
        "?": "question",
        "!": "exclamation"
    }

    NUM_LOOKUP = (
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    )

    SPECIAL_PUNC_LOOKUP = {
        "+": "heavy_plus_sign",
        "-": "heavy_minus_sign",
        "=": "heavy_equals_sign"
    }
    
    def __init__(self, caps_color: LetterColor = LetterColor.YELLOW):
        self.caps_color = caps_color

    def convert_char(self, c: str) -> str:
        if len(c) > 1 or len(c) == 0:
            raise Exception("For single-characters only!")
        elif c.isalpha():
            if c.isupper():
                return f":alphabet-{self.caps_color}-{c.lower()}:"
            else:
                return f":alphabet-{self.caps_color.invert()}-{c}:"
        elif c.isspace():
            # We like to be qUIrkY but still readable. We choose this assuming
            # most people are not using the superior dark mode.
            return ":white-small-square:"
        elif c.isnumeric():
            return f":{Emojifier.NUM_LOOKUP[int(c)]}:"
        elif c in "@#":
            return f":alphabet-{self.caps_color.invert()}-{Emojifier.PUNC_LOOKUP[c]}:"
        elif c in "?!":
            # Use caps color to maximize punctuation contrast. Again, for readability
            return f":alphabet-{self.caps_color}-{Emojifier.PUNC_LOOKUP[c]}:"
        elif c in Emojifier.SPECIAL_PUNC_LOOKUP:
            return f":{Emojifier.SPECIAL_PUNC_LOOKUP[c]}:"
        else:
            return c

    def convert_str(self, s: str) -> str:
        """
        We will not handle

        ```
        code blocks
        ```
        """
        buffer = []
        special_substr_start = None

        for c in s:
            if special_substr_start is None:
                if c in ":`":
                    special_substr_start = c
                    buffer.append(c)
                else:
                    buffer.append(self.convert_char(c))
            else:
                buffer.append(c)
                if c in ":`":
                    special_substr_start = None

        return "".join(buffer)

if __name__ == "__main__":
    print(Emojifier().convert_str(input()))
