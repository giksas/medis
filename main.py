
# -*- coding: utf-8 -*-
# coding: utf-8
from __future__ import division, print_function
import sys

def main():
    print(sys.argv[1:])
    print(sum(map(int,sys.argv[1:])))
    print("Hello World!", 5/2 == float(5)/2)

if __name__ == "__main__":
    main()
