#!/usr/bin/env python3
import json, sys, re
from pathlib import Path
import uuid


HEADLINE_PATTERN = re.compile("^(##\s-+\s+)(.+)$")
ENTRY_PATTERN = re.compile("^(.+)\s{3,}(.+)$")


def make_item(title, subtitle, heading, match=True):
    return {
        "uid": str(uuid.uuid4()),
        "title": title,
        "match": f"{heading} {title} *" if match else "*",
        "subtitle": subtitle,
        "arg": "",
        "valid": "false",
    }


def cheatsheet_as_json(cheatsheet: str) -> str:
    json_data = {"items": []}
    heading = ""
    for line in cheatsheet.split("\n"):
        line_is_entry = ENTRY_PATTERN.match(line)
        line_is_heading = HEADLINE_PATTERN.match(line)
        item = None
        if line_is_heading:
            heading = line_is_heading.group(2).capitalize()
            title = f" {heading} ".center(60, "-").upper()
            item = make_item(title, "", heading, match=False)
        elif line_is_entry:
            name = line_is_entry.group(1)
            title = f"{heading}: {name}"
            shortcut = line_is_entry.group(2)
            item = make_item(title, shortcut, heading)
        if item:
            json_data["items"].append(item)
    return json.dumps(json_data)


if __name__ == "__main__":
    filename = sys.argv[1]
    filepath = Path.home() / Path(filename)
    data = ""
    with open(filepath, "r") as cheatsheet:
        data = cheatsheet.read()
    print(cheatsheet_as_json(data))
