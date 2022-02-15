
# -*- coding: utf-8 -*-
# coding: utf-8
from __future__ import division, print_function
import sys

# Define a function `plus()`


def plus(a, b):
    return a + b

# Create a `Summation` class

    def sum(self, a, b):
        self.contents = a + b
        return self.contents


def main():
    print(sys.argv[1:])
    print('sum',sum(map(int, sys.argv[1:])))
    print('min',min(map(int, sys.argv[1:])))
    print('max',max(map(int, sys.argv[1:])))
    print(1, 1, plus(1, 3))
    print("Hello World!", 5/2 == float(5)/2)


if __name__ == "__main__":
    main()


print('pabaiga')

# & C:/Python27/python.exe c:/Users/Gabrielius/Documents/medis/main.py 1 2 3 4 5 6 7 10 