"""
Multi-threading for progress bar. Progress bar will later shows training process.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import QtDemo
import sys, time


# import model_name

class MainUi(QtWidgets.QMainWindow, QtDemo.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainUi, self).__init__(parent)
        self.setupUi(self)
        self.threadcalss = MultiThread()
        self.threadcalss.start()
        self.threadcalss.updateProgressBar.connect(self.setProgressBar)

    def setProgressBar(self, val):
        self.progressBar.setValue(val)


class MultiThread(QtCore.QThread):
    updateProgressBar = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(MultiThread, self).__init__(parent)

    def run(self):
        count = 0
        while count < 100:
            print(count)
            count += 1
            time.sleep(0.2)
            # self.emit(QtCore.pyqtSignal('value'), count)

            self.updateProgressBar.emit(count)
            # self.signals.result.emit(val)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainUi()
    window.show()
    app.exec_()
