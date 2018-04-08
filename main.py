import sys
from PyQt5.QtWidgets import QApplication
from ReadIt import ReaderWindow

app = QApplication(sys.argv)

reader = ReaderWindow()

sys.exit(app.exec_())