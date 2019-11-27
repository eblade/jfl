#!/usr/bin/env python3


import logging
import os
import uuid
from lindh.jsondb import Database

from .config import Config


class System:
    def __init__(self, root):
        self.root = root
        self.logger = logging.getLogger('jfl.system')
        self.config = Config(self.db_factory)

    def generate_id(self):
        return uuid.uuid4().hex

    def hash_filename(self, id_):
        s = str(id_)
        return os.path.join(s[:2], s[2:]) + '.json'

    def db_factory(self, name)elf.hash_filename
        path = os.path.join(self.root, name)
        return Database(path, id_generator=self.generate_id, filename_hasher=self.hash_filename)
