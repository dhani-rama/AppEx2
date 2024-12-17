# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:36:48 2024

@author: ramad
"""

from ui_diagram import Ui_mainmenu
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import Qt, QIcon
from PySide6 import QtCharts
from PySide6.QtCore import QTimer
import random


# class MySideBar(QMainWindow, Ui_mainmenu):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
        
#         self.icon_name_widget.setHidden(True)
        
#         self.btn_dashboard_1.clicked.connect(self.switch_to_dashboardPage)
#         self.btn_dashboard_2.clicked.connect(self.switch_to_dashboardPage)
        
#         self.btn_start.clicked.connect(self.update_linegraph)
        
#         # self.update_linegraph()
        
        
        
#     # switch ke different pages
#     def switch_to_dashboardPage(self):
#         self.stackedWidget.setCurrentIndex(0)
        
#     def update_linegraph(self):
        
#         chart = QtCharts.QChart()
#         chart.legend().hide()
        
#         number = ["1", "2", "3", "4", "5"]
#         lumber_number = [15, 25, 20, 30, 40]
        
#         number_series = QtCharts.QLineSeries()
#         for i in range(len(number)):
#             number_series.append(i, lumber_number[i])
            
#         chart.addSeries(number_series)
        
#         #add axis and set alignment
#         axis_x = QtCharts.QBarCategoryAxis()
#         axis_x.append(number)
#         chart.addAxis(axis_x, Qt.AlignBottom)
        
#         axis_y = QtCharts.QValueAxis()
        
#         #set minimum and maximum values for the y-axis
#         min_y = min(lumber_number)
#         max_y = max(lumber_number)
#         axis_y.setRange(min_y, max_y)
#         chart.addAxis(axis_y, Qt.AlignLeft)
        
#         number_series.attachAxis(axis_x)
#         number_series.attachAxis(axis_y)
        
#         self.line_graph_view.setChart(chart)
        



class MySideBar(QMainWindow, Ui_mainmenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.icon_name_widget.setHidden(True)
        
        self.btn_dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.btn_dashboard_2.clicked.connect(self.switch_to_dashboardPage)
        
        self.btn_start.clicked.connect(self.start_real_time_data)
        
        
        
        # Inisialisasi timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_real_time_data)
        self.data_list = []  # List untuk menyimpan data
        
    def start_real_time_data(self):
        # Mulai timer dengan interval 100 ms (0.1 detik)
        self.timer.start(100)

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def update_real_time_data(self):
        
        # Inisialisasi grafik dan timer
        self.chart = QtCharts.QChart()
        self.chart.legend().hide()
        
        self.number_series = QtCharts.QLineSeries()
        self.chart.addSeries(self.number_series)
        
        # Sumbu X dan Y
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setRange(0, 500)  # Rentang sumbu X untuk 500 titik
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setRange(0, 100)  # Set nilai Y sesuai dengan rentang data Anda
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        
        self.number_series.attachAxis(self.axis_x)
        self.number_series.attachAxis(self.axis_y)
        
        # Tampilkan grafik di view
        self.line_graph_view.setChart(self.chart)
        
        # Tambahkan data baru ke list
        new_data = random.randint(0, 100)  # Gantilah ini dengan data aktual Anda
        self.data_list.append(new_data)
        
        # Pastikan hanya menyimpan 500 data terakhir
        if len(self.data_list) > 500:
            self.data_list.pop(0)
        
        # Perbarui seri data di grafik
        self.number_series.clear()
        for i, value in enumerate(self.data_list):
            self.number_series.append(i, value)

         
