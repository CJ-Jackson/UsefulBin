#!/usr/bin/env python3
import sys


def process_args():
    for arg in sys.argv[1:]:
        print(arg.strip())


process_args()
