# GUI interface

import sys
from PyQt5.QtWidgets import QStyleFactory
from PyQt5.QtWidgets import QApplication
from myMainWindow import QmyMainWindow

app = QApplication(sys.argv)
mainform = QmyMainWindow(dbFilename='battery.db')
mainform.show()
sys.exit(app.exec_())