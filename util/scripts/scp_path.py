#!/usr/bin/env python3
import json
import os
import pathlib
import sys


def process_scp_path_config_path() -> str:
    return f"{pathlib.Path.home()}/.config/useful_bin_util/scp_path.json"


def save_scp_path_file(data: dict):
    config_path: str = process_scp_path_config_path()
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
        
        
def open_scp_path_file() -> dict:
    try:
        with open(process_scp_path_config_path(), "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        print(f"Unabled to open '{process_scp_path_config_path()}'", file=sys.stderr)
        exit(1)
        
    
def set_domain():
    try:
        domain_name: str = sys.argv[1]
        save_scp_path_file({'domain_name': domain_name})
        print(f"'{domain_name}' has been saved!")
    except IndexError:
        print("Must have one parameter", file=sys.stderr)
        exit(1)


def print_scp_path():
    try:
        username = os.getlogin()
        file_path: str = os.path.abspath(sys.argv[1])
        config: dict = open_scp_path_file()
        print(f'"{username}@{config["domain_name"]}:{file_path}"')
    except IndexError:
        print("Must have one parameter", file=sys.stderr)
        exit(1)


def process():
    command_name = os.path.basename(sys.argv[0])
    match command_name:
        case "scp_path_set_domain":
            set_domain()
        case "scp_path":
            print_scp_path()


process()
