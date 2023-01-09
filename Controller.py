from PyQt5 import QtCore, QtGui, QtWidgets
from urllib import request

class Ui_Dialog(object):
    def setupUi(self, Dialog: QtWidgets.QDialog):
        self.isOn = False
        self.turnOnOff(False)
        self.main_url = "http://192.168.1.67/"
        Dialog.setObjectName("Dialog")
        Dialog.resize(515, 408)
        Dialog.setFixedSize(515, 408)
        Dialog.setStyleSheet("QPushButton {\n"
"border: none;\n"
"    border-radius: 5px;\n"
"    background: white;\n"
"    /*background-color: rgb(137, 218, 153);*/\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 130);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 10);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 131, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Anurati")
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.turn_on = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turn_on.sizePolicy().hasHeightForWidth())
        self.turn_on.setSizePolicy(sizePolicy)
        self.turn_on.setMinimumSize(QtCore.QSize(130, 36))
        self.turn_on.setMaximumSize(QtCore.QSize(130, 36))
        self.turn_on.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.turn_on.setObjectName("turn_on")
        self.turn_on.clicked.connect(lambda: self.turnOnOff(True))
        self.horizontalLayout.addWidget(self.turn_on)
        self.turn_off = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turn_off.sizePolicy().hasHeightForWidth())
        self.turn_off.setSizePolicy(sizePolicy)
        self.turn_off.setMinimumSize(QtCore.QSize(130, 36))
        self.turn_off.setMaximumSize(QtCore.QSize(130, 36))
        self.turn_off.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.turn_off.setObjectName("turn_off")
        self.turn_off.clicked.connect(lambda: self.turnOnOff(False))
        self.horizontalLayout.addWidget(self.turn_off)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def turnOnOff(self, command: bool = False):
        condition = "ledon" if command else "ledoff"
        try:
            request.urlopen(self.main_url + condition)
        except:
            pass
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Control Builtin LED of NodeMCU over internet using Python"))
        self.label.setText(_translate("Dialog", "CONTROL LED"))
        self.turn_on.setText(_translate("Dialog", "Turn ON"))
        self.turn_off.setText(_translate("Dialog", "Turn OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
