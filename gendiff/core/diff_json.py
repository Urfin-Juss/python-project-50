import json


def generate_diff_json(file_path1, file_path2) -> str:
    with open(file_path1) as f1, open(file_path2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    diff = []

    for key in sorted(data1.keys() | data2.keys()):
        if key not in data1:
            diff.append(f"+ {key}: {data2[key]}")
        elif key not in data2:
            diff.append(f"- {key}: {data1[key]}")
        elif data1[key] != data2[key]:
            diff.append(f"- {key}: {data1[key]}")
            diff.append(f"+ {key}: {data2[key]}")

    return "\n".join(diff)
