#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from fridautils import FridaUtils
from _frida import Process


class FridaUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.frida = FridaUtils()
        self.setWindowTitle("Frida UI")
        self.resize(1440, 900)
        self.setWindowIcon(QIcon("frida.png"))
        self.root = QVBoxLayout()
        device_bar = QHBoxLayout()
        self.root.addLayout(device_bar)

        device_label = QLabel("设备")
        self.device_list = QComboBox()
        self.device_refresh = QPushButton("刷新设备")
        device_bar.addWidget(device_label)
        device_bar.addWidget(self.device_list)
        device_bar.addWidget(self.device_refresh)
        self.device_list.currentIndexChanged.connect(self.select_device_action)

        process_label = QLabel("进程")
        self.process_list = QComboBox()
        self.process_list.currentIndexChanged.connect(self.select_process_action)
        self.process_refresh = QPushButton("刷新进程")
        self.attach_process_btn = QPushButton("附加进程")
        process_pid_label = QLabel("进程id")
        self.process_pid_edt = QLineEdit()
        device_bar.addWidget(process_label)
        device_bar.addWidget(self.process_list)
        device_bar.addWidget(self.process_refresh)
        device_bar.addWidget(process_pid_label)
        device_bar.addWidget(self.process_pid_edt)
        device_bar.addWidget(self.attach_process_btn)

        app_package_label = QLabel("应用包名")
        self.app_package_edt = QLineEdit()
        self.app_spawn_btn = QPushButton("启动应用")
        device_bar.addWidget(app_package_label)
        device_bar.addWidget(self.app_package_edt)
        device_bar.addWidget(self.app_spawn_btn)

        # 将多余部分填充空白
        device_bar.addStretch(1)
        self.root.addStretch(1)

        widget = QWidget()
        widget.setLayout(self.root)
        self.setCentralWidget(widget)

        for item in self.frida.get_device_list():
            self.device_list.addItem(item)

        self.show()

    def select_device_action(self):
        device = self.device_list.currentText()
        self.statusBar().showMessage("选择设备: {}".format(device))
        self.frida.set_current_device(device)
        process_list_in_current_device = self.frida.get_process_list()
        self.process_list.clear()
        for item in process_list_in_current_device.keys():
            self.process_list.addItem(item)

    def select_process_action(self):
        process = self.process_list.currentText()
        self.statusBar().showMessage("选择进程: {}".format(process))
        process_id = 0
        process_list_in_current_device = self.frida.get_process_list()
        for item in process_list_in_current_device.keys():
            if process == item:
                proc: Process  = process_list_in_current_device[item]
                process_id = proc.pid
                self.process_pid_edt.setText("{}".format(process_id))

