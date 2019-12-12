#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from ui import FridaUI


def main():
    app = QApplication(sys.argv)
    fu = FridaUI()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
