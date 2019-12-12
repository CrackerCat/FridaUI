#!/usr/bin/env python
# -*- coding: utf-8 -*-#

# @Time    : 2019/12/12 20:08

import frida


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class FridaUtils(object):
    def __init__(self):
        self.devices = frida.enumerate_devices()

