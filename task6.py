from PyQt6 import QtWidgets
import sys
from tugas_ui import Ui_MainWindow

class Task6(QtWidgets.QMainWindow):
    def __init__(self):
        super(Task6, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setup(self)
        
        self.ui.sliderFontSize.setRange(20, 60)
        self.ui.sliderBColor.setRange(0, 255)
        self.ui.sliderFColor.setRange(0, 255)
        
        self.ui.sliderFontSize.setValue(40)
        self.ui.sliderBColor.setValue(255)
        self.ui.sliderFColor.setValue(0)
        
        self.ui.sliderFontSize.valueChanged.connect(self.changeFontSize)
        self.ui.sliderBColor.valueChanged.connect(self.changeBackgroundColor)
        self.ui.sliderFColor.valueChanged.connect(self.changeFontColor)
        
        self.changeFontSize()
        self.changeBackgroundColor()
        self.changeFontColor()
        
    def changeFontSize(self):
        fontSize = self.ui.sliderFontSize.value()
        font = self.ui.Nim.font()
        font.setPointSize(fontSize)
        self.ui.Nim.setFont(font)
            
    def changeBackgroundColor(self):
        grayValue = self.ui.sliderBColor.value()
        color = f'rgb({grayValue}, {grayValue}, {grayValue})'
        fontGray = self.ui.sliderFColor.value()
        fontColor = f'rgb({fontGray}, {fontGray}, {fontGray})'
        self.ui.Nim.setStyleSheet(f"background-color: {color}; color: {fontColor};")
            
    def changeFontColor(self):
        grayValue = self.ui.sliderFColor.value()
        color = f'rgb({grayValue}, {grayValue}, {grayValue})'
        bgGray = self.ui.sliderBColor.value()
        bgColor = f'rgb({bgGray}, {bgGray}, {bgGray})'
        self.ui.Nim.setStyleSheet(f"background-color: {bgColor}; color: {color};")

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Task6()
    window.show()
    sys.exit(app.exec())
