#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QPlainTextEdit, QMainWindow
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
        device_bar.addWidget(device_label)
        device_list = QComboBox()
        process_label = QLabel("进程")
        process_list = QComboBox()

        for item in self.frida.devices:
            device_list.addItem("{name}:{id}".format(name=item.name, id=item.id))

        device_bar.addWidget(device_list)
        device_bar.addWidget(process_label)
        device_bar.addWidget(process_list)
        device_bar.addStretch(1)

        root.addStretch(1)

        widget = QWidget()
        widget.setLayout(root)
        self.setCentralWidget(widget)

