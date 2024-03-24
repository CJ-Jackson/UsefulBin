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
    file_name: str = sys.argv[1]
    if os.path.exists(file_name):
        os.chmod(file_name, 0o755)
        return

    file_content: str
    try:
        file_content = commands[commmand_name]
    except KeyError:
        file_content = ""
        pass

    with open(file_name, "w", encoding="utf-8") as f:
        print(file_content, file=f)
    os.chmod(file_name, 0o755)


process_touch()
