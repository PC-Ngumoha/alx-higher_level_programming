#!/usr/bin/python3
"""Program that adds elements to a list stored in a file.
"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if __name__ == '__main__':
    filename = "add_item.json"
    # Load the data into the list object
    try:
        data = load_from_json_file(filename)
    except Exception:
        data = []

    # append each of the command line arguments to the list
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        data.append(sys.argv[i])

    # save the data back into the file
    save_to_json_file(data, filename)
