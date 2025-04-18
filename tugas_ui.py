from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 140, 451, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelFontColor = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelFontColor.setObjectName("labelFontColor")
        self.gridLayout.addWidget(self.labelFontColor, 2, 0, 1, 1)
        self.labelFontSize = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelFontSize.setObjectName("labelFontSize")
        self.gridLayout.addWidget(self.labelFontSize, 0, 0, 1, 1)
        self.labelBColor = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelBColor.setObjectName("labelBColor")
        self.gridLayout.addWidget(self.labelBColor, 1, 0, 1, 1)
        self.sliderFontSize = QtWidgets.QSlider(parent=self.gridLayoutWidget)
        self.sliderFontSize.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sliderFontSize.setObjectName("sliderFontSize")
        self.gridLayout.addWidget(self.sliderFontSize, 0, 1, 1, 1)
        self.sliderBColor = QtWidgets.QSlider(parent=self.gridLayoutWidget)
        self.sliderBColor.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sliderBColor.setObjectName("sliderBColor")
        self.gridLayout.addWidget(self.sliderBColor, 1, 1, 1, 1)
        self.sliderFColor = QtWidgets.QSlider(parent=self.gridLayoutWidget)
        self.sliderFColor.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sliderFColor.setObjectName("sliderFColor")
        self.gridLayout.addWidget(self.sliderFColor, 2, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 451, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Nim = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Nim.setFont(font)
        self.Nim.setAutoFillBackground(True)
        self.Nim.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Nim.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.Nim.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Nim.setObjectName("Nim")
        self.verticalLayout.addWidget(self.Nim)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lalu Rommy Rahmad Amarta Putra-F1D022058"))
        self.labelFontColor.setText(_translate("MainWindow", "Font Color"))
        self.labelFontSize.setText(_translate("MainWindow", "Font Size"))
        self.labelBColor.setText(_translate("MainWindow", "Background Color"))
        self.Nim.setText(_translate("MainWindow", "F1D022058"))
