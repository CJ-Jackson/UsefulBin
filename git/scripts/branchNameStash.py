#!/usr/bin/env python3
import json
import os
import subprocess
import sys

saveFilename: str = "bNameStash.json"


def exec_cmd(args: list) -> str:
    return subprocess.run(args, capture_output=True).stdout.decode('utf-8').strip()


class BranchNameStash:
    commandName: str
    limit: int
    gitDir: str
    currentBranchName: str

    def __init__(self):
        self.commandName = os.path.basename(sys.argv[0])
        self.limit = int(os.getenv("GIT_BRANCH_STASH_LIMIT", 10))
        self.gitDir = exec_cmd(["git", "rev-parse", "--git-dir"])
        self.currentBranchName = \
            exec_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"])

    def save_file(self, data: list):
        with open("{0}/info/{1}".format(self.gitDir, saveFilename), "w") as f:
            json.dump(data, f, ensure_ascii=False)

    def open_file(self) -> list:
        try:
            with open("{0}/info/{1}".format(self.gitDir, saveFilename), "r") as f:
                return json.load(f)
        except Exception:
            return []

    def stash_branch_name(self):
        branch_names = self.open_file()
        branch_names.insert(0, self.currentBranchName)
        self.save_file(branch_names[:self.limit])
        print("Branch name '{0}' has been stashed".format(self.currentBranchName))

    def show_stash(self):
        branch_names = self.open_file()
        key: int = 1
        for value in branch_names:
            print("{0} | {1}".format(key, value))
            key += 1

    def apply_stash(self):
        pos: int
        try:
            pos = int(sys.argv[1]) - 1
        except Exception:
            pos = 0
        branch_names = self.open_file()
        try:
            branch_name = branch_names[pos]
            if subprocess.run(["git", "rev-parse", "--verify", branch_name], capture_output=True). \
                    returncode != 0:
                raise Exception("Branch name does not exist")
            subprocess.run(["git", "checkout", branch_name])
        except Exception as e:
            print(e.args[0])

    def clear_stash(self):
        self.save_file([])

    def process_command(self):
        command: dict = {
            "gitxBStash": self.stash_branch_name,
            "gitxBStashS": self.show_stash,
            "gitxBStashA": self.apply_stash,
            "gitxBStashC": self.clear_stash
        }
        command[self.commandName]()


BranchNameStash().process_command()
