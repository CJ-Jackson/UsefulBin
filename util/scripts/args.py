#!/usr/bin/env python3
import sys


def process_args():
    for arg in sys.argv[1:]:
        print(arg.split("\n").pop(0).strip())


process_args()
