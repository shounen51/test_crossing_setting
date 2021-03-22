import time
import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils.utils import normalize_points, save_json
class btn_events():
    def __init__(self, main):
        self.main = main

    def label_press(self, point):
        self.main.win.add_point(point)

    def connect_rtsp_btn(self):
        self.main.canvasHandler.stop_playing()
        time.sleep(0.1)
        rtsp = self.main.win.ui.rtsp_edit.text()
        self.main.canvasHandler.assign_rtsp(rtsp)
        self.main.canvasHandler.start()

    def save_area_btn(self):
        w,h = self.main.canvasHandler.get_size()
        _points = self.main.win.get_draw_point()
        Npoints = [(x/w,y/h) for x,y in _points]
        areaName = "AAA"
        alertType = "1"
        day = "1111111"
        hour = "0,24"
        sec = "0"
        self.main.crossing_detector.add_area_list(areaName, Npoints, alertType, day, hour, sec)
        self.main.crossing_detector.save_area('./area.txt', "AAA")
        self.main.win.add_point(_points[0])