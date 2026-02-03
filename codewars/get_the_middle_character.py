"""
Quest: Get the Middle Character (7 Kyu)

You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"

"""

def get_middle(s):
    if len(s) % 2 == 0:
        mid_index = len(s) // 2
        return s[mid_index - 1: mid_index + 1]
    else:
        mid_index = len(s) // 2
        return s[mid_index]