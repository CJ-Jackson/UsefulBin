#!/usr/bin/env python3
import json
import os
import subprocess
import sys


def process_filename() -> str:
    tmp_dir: str = os.environ.get("XDG_RUNTIME_DIR", os.environ.get("TMPDIR", "")).rstrip("/")
    return f"{tmp_dir}/defer.json"


def save_file(command: list):
    with open(process_filename(), "w", encoding="utf-8") as f:
        json.dump(command, f)


def open_file() -> list:
    try:
        with open(process_filename(), "r", encoding="utf-8") as f:
            return json.load(f)
    except OSError:
        return []
    except json.JSONDecodeError:
        return []


def process_defer():
    commands = open_file()
    commands.append({
        "working_dir": os.getcwd(),
        "args": sys.argv[1:]
    })
    save_file(commands)


def process_start():
    commands = open_file()
    for command in commands:
        subprocess.run(command['args'], cwd=command['working_dir'])
    save_file([])
    
    
def process():
    command_name: str = os.path.basename(sys.argv[0])
    if command_name == "defer":
        process_defer()
    elif command_name == "start":
        process_start()
        
        
process()
