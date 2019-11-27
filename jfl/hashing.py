#!/usr/bin/env python3


from hashlib import sha256 as algorithm


HASHING_SIZE = 4096


def calculate_hash(filepath):
    hasher = algorithm()

    with open(filepath, 'rb') as f:
        data = f.read(HASHING_SIZE)
        hasher.update(data)
    
    return hasher.hexdigest()


if __name__ == '__main__':
    import sys
    import os
    from .scanning import scan_folder_recursively

    assert len(sys.argv) == 2, "Missing argument PATH"
    root = sys.argv[1]
    counter = 0

    for fullpath in scan_folder_recursively(root):
        thehash = calculate_hash(fullpath)
        print(fullpath, thehash)
        counter += 1

    print('Calculated', counter, 'hashes')
