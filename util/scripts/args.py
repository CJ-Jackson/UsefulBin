#!/usr/bin/env python3
import sys


def process_args():
    for arg in sys.argv[1:]:
        print(arg.strip())


if __name__ == "__main__":
    process_args()
