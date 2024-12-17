# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:11:44 2024

@author: ramad
"""

from PySide6.QtWidgets import QApplication
import sys
from sidebar import MySideBar

app = QApplication.instance()

if app is None:  # Jika belum ada, buat instance baru
    app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec()