#!/usr/bin/env python3


import sys
import os

from hashlib import sha256 as algorithm


HASHING_SIZE = 4096


def get_hash(filepath):
    hasher = algorithm()

    with open(filepath, 'rb') as f:
        data = f.read(HASHING_SIZE)
        hasher.update(data)
    
    return hasher.hexdigest()


if __name__ == '__main__':
    assert len(sys.argv) == 2, "Missing argument PATH"
    root = sys.argv[1]
    counter = 0

    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            fullpath = os.path.join(root, dirpath, filename)
            thehash = get_hash(fullpath)
            print(fullpath, thehash)
            counter += 1

    print('Did', counter, 'hashes')
