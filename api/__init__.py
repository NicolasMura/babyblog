# -*- coding: utf-8 -*-
from __future__ import unicode_literals

VERSION = (1, 0, 0)


def get_version(version=None):
    return '.'.join(map(str, VERSION))

__version__ = get_version(VERSION)
