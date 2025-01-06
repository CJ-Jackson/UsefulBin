#!/usr/bin/env python3
import pathlib
import subprocess
import time

script_name = f"/tmp/useful_write_exec_{time.time()}"

script_path = pathlib.Path(script_name)
script_path.write_text("#!/bin/dash\n\n", "utf-8")
script_path.chmod(0o700)

subprocess.run(["nvim", script_name])
subprocess.run([script_name])