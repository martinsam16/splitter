# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 293)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.spinMinStart = QtWidgets.QSpinBox(Dialog)
        self.spinMinStart.setGeometry(QtCore.QRect(50, 91, 51, 21))
        self.spinMinStart.setObjectName("spinMinStart")
        self.spinSecStart = QtWidgets.QSpinBox(Dialog)
        self.spinSecStart.setGeometry(QtCore.QRect(100, 91, 51, 21))
        self.spinSecStart.setMinimum(1)
        self.spinSecStart.setObjectName("spinSecStart")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 71, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 51, 21))
        self.label_2.setObjectName("label_2")
        self.inptPathVideo = QtWidgets.QTextEdit(Dialog)
        self.inptPathVideo.setGeometry(QtCore.QRect(30, 30, 271, 31))
        self.inptPathVideo.setObjectName("inptPathVideo")
        self.inptOutputFolder = QtWidgets.QTextEdit(Dialog)
        self.inptOutputFolder.setEnabled(True)
        self.inptOutputFolder.setGeometry(QtCore.QRect(30, 150, 271, 31))
        self.inptOutputFolder.setObjectName("inptOutputFolder")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 130, 71, 16))
        self.label_4.setObjectName("label_4")
        self.spinSecEnd = QtWidgets.QSpinBox(Dialog)
        self.spinSecEnd.setGeometry(QtCore.QRect(220, 91, 51, 21))
        self.spinSecEnd.setMinimum(1)
        self.spinSecEnd.setObjectName("spinSecEnd")
        self.spinMinEnd = QtWidgets.QSpinBox(Dialog)
        self.spinMinEnd.setGeometry(QtCore.QRect(170, 91, 51, 21))
        self.spinMinEnd.setMinimum(0)
        self.spinMinEnd.setProperty("value", 0)
        self.spinMinEnd.setObjectName("spinMinEnd")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(170, 71, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(220, 70, 51, 21))
        self.label_8.setObjectName("label_8")
        self.checkBoxSpeechRecognition = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSpeechRecognition.setGeometry(QtCore.QRect(190, 210, 111, 17))
        self.checkBoxSpeechRecognition.setObjectName("checkBoxSpeechRecognition")
        self.doubleSpinSimilarity = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinSimilarity.setGeometry(QtCore.QRect(30, 210, 62, 22))
        self.doubleSpinSimilarity.setMaximum(1.0)
        self.doubleSpinSimilarity.setProperty("value", 0.9)
        self.doubleSpinSimilarity.setObjectName("doubleSpinSimilarity")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 190, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(110, 190, 71, 16))
        self.label_10.setObjectName("label_10")
        self.spinSecSplit = QtWidgets.QSpinBox(Dialog)
        self.spinSecSplit.setGeometry(QtCore.QRect(110, 210, 51, 21))
        self.spinSecSplit.setProperty("value", 30)
        self.spinSecSplit.setObjectName("spinSecSplit")
        self.pushButtonOk = QtWidgets.QPushButton(Dialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(230, 240, 71, 31))
        self.pushButtonOk.setObjectName("pushButtonOk")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Splitter"))
        self.label.setText(_translate("Dialog", "Min"))
        self.label_2.setText(_translate("Dialog", "Sec"))
        self.label_3.setText(_translate("Dialog", "Input Video"))
        self.label_4.setText(_translate("Dialog", "Output Folder"))
        self.label_7.setText(_translate("Dialog", "Min"))
        self.label_8.setText(_translate("Dialog", "Sec"))
        self.checkBoxSpeechRecognition.setText(_translate("Dialog", "Speech recognition"))
        self.label_9.setText(_translate("Dialog", "% similarity"))
        self.label_10.setText(_translate("Dialog", "Seconds split"))
        self.pushButtonOk.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
