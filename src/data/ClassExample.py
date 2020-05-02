"""Flight class example
in python
"""

class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f"Invalid value found '{number}' ")
        self._number = number


    def number(self):
        return "SH494"


