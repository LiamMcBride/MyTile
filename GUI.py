from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
   def __init__(self):
       super().__init__()

       self.setGeometry(200, 200, 1800, 1200)
       self.setWindowTitle("PyQt5 window")
       self.show()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())