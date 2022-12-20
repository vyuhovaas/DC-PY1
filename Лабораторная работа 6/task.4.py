import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    list_dict = []
    with open(filename) as f:
        header_list = f.readline().replace(new_line, "").split(delimiter)
        for line in f:
            list_dict.append(dict(zip(header_list, line.replace(new_line, "").split(delimiter))))
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
