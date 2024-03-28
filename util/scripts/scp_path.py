#!/usr/bin/env python3
import json
import os
import pathlib
import sys


def process_config_path() -> str:
    return f"{pathlib.Path.home()}/.config/useful_bin_util/scp_path.json"


def save_file(data: dict):
    config_path: str = process_config_path()
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
        
        
def open_file() -> dict:
    config_path: str = process_config_path()
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except OSError:
        print(f"Unable to open '{config_path}'", file=sys.stderr)
        exit(1)
    except json.JSONDecodeError:
        print(f"Unable to decode '{config_path}'", file=sys.stderr)
        exit(1)
        
        
def set_domain():
    try:
        domain_name: str = sys.argv[1]
        save_file({'domain_name': domain_name})
        print(f"'{domain_name}' has been saved!")
    except IndexError:
        print("Must have one parameter", file=sys.stderr)
        exit(1)


def print_scp_path():
    try:
        username = os.getlogin()
        file_path: str = os.path.abspath(sys.argv[1])
        config: dict = open_file()
        print(f'"{username}@{config["domain_name"]}:{file_path}"')
    except IndexError:
        print("Must have one parameter", file=sys.stderr)
        exit(1)


def process():
    command_name = os.path.basename(sys.argv[0])
    if command_name == "scp_path_set_domain":
        set_domain()
    elif command_name == "scp_path":
        print_scp_path()


process()
