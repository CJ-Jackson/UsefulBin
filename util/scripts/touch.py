#!/usr/bin/env python3
import os.path
import sys

commands: dict = {
    "touch_sh": '''#!/usr/bin/env sh
cd $(dirname $(realpath -s $0))''',

    "touch_py": '#!/usr/bin/env python3',
    "touch_toml": '#!/usr/bin/env name_of_app'
}


def process_touch():
    commmand_name: str = os.path.basename(sys.argv[0])
    
    file_name: str
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Must have one argument", file=sys.stderr)
        exit(1)

    if os.path.exists(file_name):
        return

    file_content: str = commands.get(commmand_name, "")

    with open(file_name, "w", encoding="utf-8") as f:
        print(file_content, file=f)
    os.chmod(file_name, 0o755)


if __name__ == "__main__":
    process_touch()
