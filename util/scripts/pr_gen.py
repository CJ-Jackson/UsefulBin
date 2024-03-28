#!/usr/bin/env python3
import json
import os
import pathlib
import sys
import time
import tomllib

toml_template = '''\
jira_task_number = []

[links]
Linked_PR = []
Related_PR = []

[checks]
CMS = false
DB = false
Live_Follow-up = false
Parameters = false'''


def process_config_path() -> str:
    return f"{pathlib.Path.home()}/.config/useful_bin_util/pr_gen.json"


def save_config_file(data: dict):
    config_path: str = process_config_path()
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(data, f)


def open_config_file() -> dict:
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


def set_jira_prefix():
    try:
        jira_prefix: str = sys.argv[1]
        save_config_file({"jira_prefix": jira_prefix})
        print(f"Save jira prefix '{jira_prefix}'")
    except IndexError:
        print("Must have one parameter", file=sys.stderr)
        exit(1)
        

def process_tmp_path() -> str:
    tmp_dir: str = os.environ.get("XDG_RUNTIME_DIR", os.environ.get("TMPDIR", "")).rstrip("/")
    return f"{tmp_dir}/pr_{time.time()}.toml"


def create_template():
    tmp_path = process_tmp_path()
    with open(tmp_path, "w", encoding="utf-8") as f:
        print(toml_template, file=f)
    print(tmp_path)


def open_pr_config() -> dict:
    try:
        tmp_path: str = sys.argv[1]
        with open(tmp_path, "r", encoding="utf-8") as f:
            return tomllib.loads(f.read())
    except (OSError, KeyError):
        print("Unabled to process P.R. config", file=sys.stderr)
        exit(1)


def create_pr():
    pr = open_pr_config()
    gl = open_config_file()
    body: str = "| **Q** | **A** |\n|---|---|\n"
    
    first: str = "JIRA"
    for task in pr['jira_task_number']:
        body += f"| {first} | [{task}]({gl['jira_prefix']}/{task}) |\n"
        first = ""
    
    for key, links in pr['links'].items():
        key = key.replace("_", " ")
        first: str = key
        for link in links:
            body += f"| {first} | {link} |\n"
            first = ""
            
    for key, value in pr['checks'].items():
        key = key.replace("_", " ")
        check: str = ":heavy_multiplication_x:"
        if value:
            check = ":heavy_check_mark:"
        body += f"| {key} | {check} |\n"
        
    body += '''
# Description

# How to test'''
            
    print(body)
            
    
def process():
    command_name = os.path.basename(sys.argv[0])
    if command_name == "pr_gen_set_jira_prefix":
        set_jira_prefix()
    elif command_name == "pr_gen_create_template":
        create_template()
    elif command_name == "pr_gen_create_pr":
        create_pr()
        
        
process()
