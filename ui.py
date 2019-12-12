#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QLineEdit, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from fridautils import FridaUtils


class FridaUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.frida = FridaUtils()
        self.setup_ui()
        self.show()

    def setup_ui(self):

        self.statusBar().showMessage('Ready')
        self.setWindowTitle("Frida UI")
        self.resize(1440, 900)
        self.setWindowIcon(QIcon("frida.png"))
        root = QVBoxLayout()
        device_bar = QHBoxLayout()
        root.addLayout(device_bar)

        device_label = QLabel("设备")
        device_list = QComboBox()
        device_refresh = QPushButton("刷新设备")
        device_bar.addWidget(device_label)
        device_bar.addWidget(device_list)
        device_bar.addWidget(device_refresh)

        process_label = QLabel("进程")
        process_list = QComboBox()
        process_refresh = QPushButton("刷新进程")
        attach_process_btn = QPushButton("附加进程")
        process_pid_label = QLabel("进程id")
        process_pid_edt = QLineEdit()
        device_bar.addWidget(process_label)
        device_bar.addWidget(process_list)
        device_bar.addWidget(process_refresh)
        device_bar.addWidget(process_pid_label)
        device_bar.addWidget(process_pid_edt)
        device_bar.addWidget(attach_process_btn)

        for item in self.frida.devices:
            device_list.addItem("{name}:{id}".format(name=item.name, id=item.id))

        app_package_label = QLabel("应用包名")
        app_package_edt = QLineEdit()
        app_spawn_btn = QPushButton("启动应用")
        device_bar.addWidget(app_package_label)
        device_bar.addWidget(app_package_edt)
        device_bar.addWidget(app_spawn_btn)

        # 将多余部分填充空白
        device_bar.addStretch(1)

        root.addStretch(1)

        widget = QWidget()
        widget.setLayout(root)
        self.setCentralWidget(widget)

