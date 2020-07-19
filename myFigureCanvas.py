# -*- coding: utf-8 -*-
"""
myFigureCanvas.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Figure canvas for the GUI interface.

"""

from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout

from PyQt5.QtCore import *

import matplotlib as mpl

from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


class QmyFigureCanvas(QWidget):

    # self.widget = QWidget()

    def __init__(self, parent=None, toolbarVisible=True, showHint=False):
        super().__init__(parent)

        self.figure = mpl.figure.Figure(figsize=(50, 50))
        figCanvas = FigureCanvas(self.figure)
        # scroll = QScrollArea(self.widget)
        # self.scroll.setWidget(figCanvas)

        self.naviBar = NavigationToolbar(figCanvas, self)

        actList = self.naviBar.actions()
        count = len(actList)
        self.__lastActtionHint = actList[count - 1]
        self.__showHint = showHint
        self.__lastActtionHint.setVisible(self.__showHint)
        self.__showToolbar = toolbarVisible
        self.naviBar.setVisible(self.__showToolbar)

        layout = QVBoxLayout(self)
        layout.addWidget(self.naviBar)
        layout.addWidget(figCanvas)
        # layout.addWidget(scroll)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(0)

        self.__cid = figCanvas.mpl_connect("scroll_event", self.do_scrollZoom)

# =====Public interface
    def setToolbarVisible(self, isVisible=True):
        self.__showToolbar = isVisible
        self.naviBar.setVisible(isVisible)

    def setDataHintVisible(self, isVisible=True):
        self.__showHint = isVisible
        self.__lastActtionHint.setVisible(isVisible)

    def redraw(self):
        self.figure.canvas.draw()

    def do_scrollZoom(self, event):
        ax = event.inaxes
        if ax is None:
            return

        # Push the current view limits and position onto the stack，这样才可以还原
        self.naviBar.push_current()
        xmin, xmax = ax.get_xbound()
        xlen = xmax - xmin
        ymin, ymax = ax.get_ybound()
        ylen = ymax - ymin

        # step [scalar],positive = ’up’, negative ='down'
        xchg = event.step * xlen / 20
        xmin = xmin + xchg
        xmax = xmax - xchg
        ychg = event.step * ylen / 20
        ymin = ymin + ychg
        ymax = ymax - ychg

        ax.set_xbound(xmin, xmax)
        ax.set_ybound(ymin, ymax)
        event.canvas.draw()
