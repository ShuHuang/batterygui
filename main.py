# GUI main interface

import sys

from PyQt5.QtWidgets import QApplication

from myMainWindow import QmyMainWindow
from fbs_runtime.application_context.PyQt5 import ApplicationContext


appctxt = ApplicationContext()  # Create GUI Application
db = appctxt.get_resource('battery_revision.db')
form = QmyMainWindow(dbFilename=db)  # Create Window
form.show()
sys.exit(appctxt.app.exec_())
