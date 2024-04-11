#!/usr/bin/env python3
import os.path
import subprocess
import sys

script_path = os.path.abspath(sys.argv[1])
working_directory = os.path.dirname(script_path)
subprocess.run(["dash", script_path], cwd=working_directory)
