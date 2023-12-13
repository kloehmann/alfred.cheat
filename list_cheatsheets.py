import json
import sys, os
from pathlib import Path

CHEAT_DIR = Path.home() / Path(os.environ["cheatdir"])


def cheatsheet_list(filter_str):
    cheatsheets = CHEAT_DIR.glob("*")

    json_data = {"items": []}
    for c in cheatsheets:
        c = str(c.relative_to(CHEAT_DIR))
        if filter_str and filter_str.lower() not in c.lower():
            continue

        json_data["items"].append({"title": c, "arg": c})
    return json.dumps(json_data)


if __name__ == "__main__":
    filter_str = sys.argv[1] if len(sys.argv) > 1 else None
    print(cheatsheet_list(filter_str))
