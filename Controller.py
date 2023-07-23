from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from packages import *
import resources_rc

REQUEST_URL: str = "http://192.168.1.75/%s"


class Ui_Dialog(object):
    def update_status(self, success: bool | None = None):
        if isinstance(success, bool):
            background = SUCCESS if success else FAILED
        else:
            background = WARNING
        self.status.setStyleSheet("""
            #status{
                background: %s
            }
        """ % background)

    def toggleLED(self, turn_on: bool = False) -> bool:
        param = '1' if turn_on else '0'
        try:
            content = requests.get(REQUEST_URL % param).text.strip()
            self.update_status(content == 'ON')
            return True
        except Exception as e:
            print(str(e))
            self.update_status(None)
            return False

    def setupUi(self, Dialog):
        QtGui.QFontDatabase.addApplicationFont('./assets/fonts/Anurati.otf')
        QtGui.QFontDatabase.addApplicationFont('./assets/fonts/Poppins.ttf')
        Dialog.setObjectName("Dialog")
        Dialog.resize(515, 408)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/Favicon.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off
        )
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(STYLESHEET)

        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.turn_on = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.turn_on.sizePolicy().hasHeightForWidth())
        self.turn_on.setSizePolicy(sizePolicy)
        self.turn_on.setMinimumSize(QtCore.QSize(130, 36))
        self.turn_on.setMaximumSize(QtCore.QSize(130, 36))
        self.turn_on.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.turn_on.setObjectName("turn_on")
        self.turn_on.clicked.connect(lambda *a, **b: self.toggleLED(True))
        self.horizontalLayout.addWidget(self.turn_on)

        self.turn_off = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.turn_off.sizePolicy().hasHeightForWidth())
        self.turn_off.setSizePolicy(sizePolicy)
        self.turn_off.setMinimumSize(QtCore.QSize(130, 36))
        self.turn_off.setMaximumSize(QtCore.QSize(130, 36))
        self.turn_off.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.turn_off.setObjectName("turn_off")
        self.turn_off.clicked.connect(lambda *a, **b: self.toggleLED(False))
        self.horizontalLayout.addWidget(self.turn_off)

        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(
            20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(
            20, 87, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)

        self.status = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setMinimumSize(QtCore.QSize(25, 25))
        self.status.setMaximumSize(QtCore.QSize(50, 50))
        self.status.setText("")
        self.status.setObjectName("status")
        self.horizontalLayout_2.addWidget(self.status)

        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)

        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.title = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Anurati")
        font.setPointSize(26)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 0, 1, 1)

        self.context = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.context.setFont(font)
        self.context.setAlignment(QtCore.Qt.AlignCenter)
        self.context.setObjectName("context")
        self.gridLayout.addWidget(self.context, 2, 0, 1, 1)

        spacerItem7 = QtWidgets.QSpacerItem(
            20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 6, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Control LED"))
        self.turn_on.setText(_translate("Dialog", "Turn ON"))
        self.turn_off.setText(_translate("Dialog", "Turn OFF"))
        self.title.setText(_translate("Dialog", "CONTROL LED"))
        self.context.setText(_translate(
            "Dialog", "Control Builtin LED of NodeMCU over internet using Python"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
