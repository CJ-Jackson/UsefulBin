#!/usr/bin/env python3
import json
import os
import subprocess
import sys

saveFilename: str = "bNameStash.json"


def exec_cmd(args: list) -> str:
    return subprocess.run(args, capture_output=True).stdout.decode('utf-8').strip()


class BranchNameStash:
    command_name: str
    limit: int
    git_dir: str
    current_branch_name: str

    def __init__(self):
        self.command_name = os.path.basename(sys.argv[0])
        self.limit = int(os.getenv("GIT_BRANCH_STASH_LIMIT", 10))
        self.git_dir = exec_cmd(["git", "rev-parse", "--git-dir"])
        self.current_branch_name = \
            exec_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"])

    def save_file(self, data: list):
        with open(f"{self.git_dir}/info/{saveFilename}", "w") as f:
            json.dump(data, f, ensure_ascii=False)

    def open_file(self) -> list:
        try:
            with open(f"{self.git_dir}/info/{saveFilename}", "r") as f:
                return json.load(f)
        except OSError:
            return []
        except json.JSONDecodeError:
            return []

    def stash_branch_name(self):
        branch_names = self.open_file()
        branch_names.insert(0, self.current_branch_name)
        self.save_file(branch_names[:self.limit])
        print(f"Branch name '{self.current_branch_name}' has been stashed")

    def show_stash(self):
        branch_names = self.open_file()
        key: int = 1
        padding: int = len(str(len(branch_names)))
        for value in branch_names:
            print(f" {key: >{padding}} | {value}")
            key += 1

    def apply_stash(self):
        pos: int
        try:
            pos = int(sys.argv[1]) - 1
        except IndexError:
            pos = 0
        branch_names = self.open_file()
        try:
            branch_name = branch_names[pos]
            subprocess.run(["git", "rev-parse", "--verify", branch_name], capture_output=True).check_returncode()
            subprocess.run(["git", "checkout", branch_name])
        except KeyError:
            print(f"Branch key value '{pos+1}' does not exist", file=sys.stderr)
            exit(1)
        except subprocess.CalledProcessError:
            print("Branch name does not exist", file=sys.stderr)
            exit(1)

    def clear_stash(self):
        self.save_file([])

    def process_command(self):
        command: dict = {
            "_gitBStash": self.stash_branch_name,
            "_gitBStashS": self.show_stash,
            "_gitBStashA": self.apply_stash,
            "_gitBStashC": self.clear_stash
        }

        try:
            command[self.command_name]()
        except KeyError:
            print(f"Command {self.command_name} does not exist", file=sys.stderr)


if __name__ == "__main__":
    BranchNameStash().process_command()
