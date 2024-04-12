#!/usr/bin/env python3
import json
import os
import pathlib
import sys
import time
import tomllib

toml_template = '''\
jira_task_number = ['']

[links]
Linked_PR = []
Related_PR = []

[checks]
CMS = false
DB = false
Live_Follow-up = false
Parameters = false'''


def process_pr_gen_config_path() -> str:
    return f"{pathlib.Path.home()}/.config/useful_bin_util/pr_gen.json"


def save_pr_gen_config_file(data: dict):
    config_path: str = process_pr_gen_config_path()
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(data, f)


def open_pr_gen_config_file() -> dict:
    config_path: str = process_pr_gen_config_path()
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        print(f"Unabled to open '{config_path}'", file=sys.stderr)
        exit(1)


def set_jira_prefix():
    try:
        jira_prefix: str = sys.argv[1]
        save_pr_gen_config_file({"jira_prefix": jira_prefix})
        print(f"Save jira prefix '{jira_prefix}'")
    except IndexError:
        print("Must have one parameter", file=sys.stderr)
        exit(1)
        

def process_pr_gen_tmp_path() -> str:
    tmp_dir: str = os.environ.get("XDG_RUNTIME_DIR", os.environ.get("TMPDIR", "")).rstrip("/")
    return f"{tmp_dir}/pr_{time.time()}.toml"


def create_template():
    tmp_path = process_pr_gen_tmp_path()
    with open(tmp_path, "w", encoding="utf-8") as f:
        print(toml_template, file=f)
    print(tmp_path)


def open_pr_config() -> dict:
    try:
        tmp_path: str = sys.argv[1]
        with open(tmp_path, "rb") as f:
            return tomllib.load(f)
    except (OSError, KeyError):
        print("Unabled to process P.R. config", file=sys.stderr)
        exit(1)


class MaxLenght:
    __max_lenght: dict[str, int]

    def __init__(self):
        self.__max_lenght = {}

    def set(self, name: str, value: str):
        lenght = len(value)
        if lenght > self.__max_lenght.get(name, 5):
            self.__max_lenght[name] = lenght

    def get(self, name) -> int:
        return self.__max_lenght.get(name, 5)


def create_pr():
    pr_config = open_pr_config()
    gl_config = open_pr_gen_config_file()
    max_lenght = MaxLenght()
    header_list: list[dict] = [{"key": "**Q**", "value": "**A**"}]
    body_list: list[dict[str, str]] = []
    body: str = ""
    
    first: str = "JIRA"
    max_lenght.set("key", first)
    for task in pr_config['jira_task_number']:
        value_ = f"[{task}]({gl_config['jira_prefix']}/{task})"
        max_lenght.set("value", value_)
        body_list.append({"key": first, "value": value_})
        first = ""

    for key, links in pr_config['links'].items():
        key = key.replace("_", " ")
        first: str = key
        max_lenght.set("key", first)
        for link in links:
            max_lenght.set("value", link)
            body_list.append({"key": first, "value": link})
            first = ""

    for key, value in pr_config['checks'].items():
        key = key.replace("_", " ")
        max_lenght.set("key", key)
        check: str = ":heavy_multiplication_x:"
        if value:
            check = ":heavy_check_mark:"
        max_lenght.set("value", check)
        body_list.append({"key": key, "value": check})

    key_lenght = max_lenght.get("key")
    value_lenght = max_lenght.get("value")
    header_list.append({
        "key": ":" + ("-"*(key_lenght+1)),
        "value": ":" + ("-"*(value_lenght+1)),
        "line": True
    })

    for header in header_list:
        key_ = header["key"]
        value_ = header["value"]
        if not header.get("line", False):
            body += f"| {key_: <{key_lenght}} | {value_: <{value_lenght}} |\n"
        else:
            body += f"|{key_}|{value_}|\n"

    for body_item in body_list:
        key_ = body_item["key"]
        value_ = body_item["value"]
        body += f"| {key_: <{key_lenght}} | {value_: <{value_lenght}} |\n"
        
    body += '''
# Description

# How to test'''
            
    print(body)
            
    
def process():
    command_name = os.path.basename(sys.argv[0])
    match command_name:
        case "pr_gen_set_jira_prefix":
            set_jira_prefix()
        case "pr_gen_create_template":
            create_template()
        case "pr_gen_create_pr":
            create_pr()
        

if __name__ == "__main__":
    process()
