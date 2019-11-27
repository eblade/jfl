#!/usr/bin/env python3

import os
import sys

from jfl.system import System
from jfl.config import (
    ResolutionConfigValue,
    ServerConfigValue,
    MediaConfigValue,
)


if __name__ == '__main__':
    assert len(sys.argv) == 2, "Missing argument PATH"
    root = sys.argv[1]

    system = System(root)
    system.config['import.resolution'] = ResolutionConfigValue()
    system.config['import.server'] = ServerConfigValue()
    system.config['media'] = MediaConfigValue(mount_path='/run/media')
