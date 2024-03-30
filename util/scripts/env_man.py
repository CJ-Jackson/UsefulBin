#!/usr/bin/env python3
import pathlib
import sys
import tomllib


def env_man_config_path() -> str:
    return f"{pathlib.Path.home()}/.config/useful_bin_util/env_man.toml"


def open_env_man_config() -> dict:
    try:
        with open(env_man_config_path(), "r", encoding="utf-8") as f:
            return tomllib.loads(f.read())
    except (OSError, tomllib.TOMLDecodeError):
        print(f"Unabled to open '{env_man_config_path()}'", file=sys.stderr)
        exit(1)
        
        
def process_env_man():
    config_ = open_env_man_config()
    all_path: list | str = []
    all_env: dict = {}
    
    for arg in sys.argv[1:]:
        if arg in config_:
            arg_config = config_[arg]
            if 'path' in arg_config:
                all_path.append(arg_config['path'])
            if 'env' in arg_config:
                all_env |= arg_config['env']
    
    if len(all_path) > 0:
        all_path = ":".join(all_path)
        print(f'export PATH="{all_path}:$PATH"')
        
    for name, value in all_env.items():
        print(f'export {name}="{value}"')


process_env_man()