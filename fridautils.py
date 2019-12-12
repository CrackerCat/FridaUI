#!/usr/bin/env python
# -*- coding: utf-8 -*-#

# @Time    : 2019/12/12 20:08

import frida
from frida.core import Device
from _frida import Process
from PyQt5.QtWidgets import QMessageBox


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
        self.current_device: Device = None
        self.current_process: Process = None
        self.current_package = None
        self.current_platform = None
        self.session = None

        self.devices = {}
        self.processes = {}

    def get_device_list(self):
        self.devices = {}
        for item in frida.enumerate_devices():
            key = "{name}:{id}".format(name=item.name, id=item.id)
            key = key.strip()
            self.devices[key] = item
        return self.devices

    def set_current_device(self, device_name):
        if self.devices.keys().__contains__(device_name):
            self.current_device = self.devices[device_name]
        else:
            QMessageBox.critical("错误", "设备断开，或者无法附加，尝试使用管理员权限运行")

    def get_process_list(self):
        if self.current_device:
            self.processes = {}
            for item in self.current_device.enumerate_processes():
                key = "{pid}:{name}".format(pid=item.pid, name=item.name)
                key = key.strip()
                self.processes[key] = item
            return self.processes
        else:
            QMessageBox.critical("错误", "没有默认设备")

    def set_current_process(self):
        pass
