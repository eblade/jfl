#!/usr/bin/env python3

import os


def scan_folder_recursively(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            yield os.path.join(path, dirpath, filename)



if __name__ == '__main__':
    import sys
    import os

    assert len(sys.argv) == 2, "Missing argument PATH"
    root = sys.argv[1]

    for path in scan_folder_recursively(root):
        print(path)
