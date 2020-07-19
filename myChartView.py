# -*- coding: utf-8 -*-
"""
myChartView.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chart view for the GUI.

"""

from PyQt5.QtWidgets import QGraphicsView

from PyQt5.QtCore import pyqtSignal, QPoint, Qt, QRectF

from PyQt5.QtGui import QMouseEvent, QKeyEvent, QFont

from PyQt5.QtChart import QChartView


class QmyChartView(QChartView):

    mouseMove = pyqtSignal(QPoint)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.RubberBandDrag)

        self.__beginPoint = QPoint()
        self.__endPoint = QPoint()


# ========== event handling============


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__beginPoint = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        point = event.pos()
        self.mouseMove.emit(point)
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__endPoint = event.pos()
            rectF = QRectF()
            rectF.setTopLeft(self.__beginPoint)
            rectF.setBottomRight(self.__endPoint)
            self.chart().zoomIn(rectF)
        elif event.button() == Qt.RightButton:
            self.chart().zoomReset()

        super().mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Plus:
            self.chart().zoom(1.2)
        elif key == Qt.Key_Minus:
            self.chart().zoom(0.8)
        elif key == Qt.Key_Left:
            self.chart().scroll(10, 0)
        elif key == Qt.Key_Right:
            self.chart().scroll(-10, 0)
        elif key == Qt.Key_Up:
            self.chart().scroll(0, -10)
        elif key == Qt.Key_Down:
            self.chart().scroll(0, 10)
        elif key == Qt.Key_PageUp:
            self.chart().scroll(0, -50)
        elif key == Qt.Key_PageDown:
            self.chart().scroll(0, 50)
        elif key == Qt.Key_Home:
            self.chart().zoomReset()

        super().keyPressEvent(event)
