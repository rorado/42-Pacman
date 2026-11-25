import json


def parse(config_path: str) -> dict:
    content = ""
    comments = ("#", "//")

    with open(config_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.lstrip().startswith(comments):
                continue

            content += line

    config = json.loads(content)
    print(json.dumps(config, indent=2))
    return config