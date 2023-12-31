# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1509, 938)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("QMainWindow, QWidget {\n"
"    background-color: rgb(47, 47, 47);\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(2, 152, 120);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(2, 152, 120);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 450, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.radioButton.setStyleSheet("QRadioButton {\n"
"    color:rgb(147, 147, 147);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 2px solid rgb(4, 192, 157);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 480, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.radioButton_2.setStyleSheet("QRadioButton {\n"
"    color: rgb(147, 147, 147);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 2px solid rgb(4, 192, 157);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 130, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"        color: rgb(4, 192, 157);\n"
"    outline: none;\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"    }\n"
"QTableWidget::item:selected {\n"
"    background-color: transparent;\n"
"    color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:selected QLineEdit {\n"
"  color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:focus {\n"
"        border: none;\n"
"    }\n"
"QLineEdit:focus {\n"
"    border: none;\n"
"}")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(37)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(40, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("QSpinBox::up-arrow {\n"
"    image: url(up.png);\n"
"}\n"
"QSpinBox::down-arrow {\n"
"    image: url(down.png);\n"
"}\n"
"QSpinBox:hover {\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"}\n"
"QSpinBox:focus {\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"}\n"
"QSpinBox {\n"
"    selection-background-color: transparent;\n"
"    selection-color: rgb(4, 192, 157);\n"
"    color: rgb(147, 147, 147);\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"}")
        self.spinBox.setReadOnly(False)
        self.spinBox.setAccelerated(False)
        self.spinBox.setMaximum(20)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(190, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet("QSpinBox::up-arrow {\n"
"    image: url(up.png);\n"
"}\n"
"QSpinBox::down-arrow {\n"
"    image: url(down.png);\n"
"}\n"
"QSpinBox:hover {\n"
"    border: 1px solid rgb(147, 147, 147);\n"
"}\n"
"QSpinBox:focus {\n"
"    border: 1px solid rgb(147, 147, 147);\n"
"}\n"
"QSpinBox {\n"
"    selection-background-color: transparent;\n"
"    selection-color: rgb(4, 192, 157);\n"
"    color: rgb(147, 147, 147);\n"
"}")
        self.spinBox_2.setMaximum(20)
        self.spinBox_2.setObjectName("spinBox_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(390, 130, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setAutoFillBackground(False)
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
"        color: rgb(4, 192, 157);\n"
"    outline: none;\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"    }\n"
"QTableWidget::item:selected {\n"
"    background-color: transparent;\n"
"    color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:selected QLineEdit {\n"
"  color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:focus {\n"
"        border: none;\n"
"    }\n"
"QLineEdit:focus {\n"
"    border: none;\n"
"}")
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(37)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(740, 130, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setAutoFillBackground(False)
        self.tableWidget_3.setStyleSheet("QTableWidget {\n"
"        color: rgb(4, 192, 157);\n"
"    outline: none;\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"    }\n"
"QTableWidget::item:selected {\n"
"    background-color: transparent;\n"
"    color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:selected QLineEdit {\n"
"  color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:focus {\n"
"        border: none;\n"
"    }\n"
"QLineEdit:focus {\n"
"    border: none;\n"
"}")
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_3.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_3.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(37)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 95, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(147, 147, 147);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 95, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(147, 147, 147);")
        self.label_2.setObjectName("label_2")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(1080, 130, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setAutoFillBackground(False)
        self.tableWidget_4.setStyleSheet("QTableWidget {\n"
"        color: rgb(4, 192, 157);\n"
"    outline: none;\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"    }\n"
"QTableWidget::item:selected {\n"
"    background-color: transparent;\n"
"    color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:selected QLineEdit {\n"
"  color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:focus {\n"
"        border: none;\n"
"    }\n"
"QLineEdit:focus {\n"
"    border: none;\n"
"}")
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_4.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_4.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.horizontalHeader().setVisible(False)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(37)
        self.tableWidget_4.horizontalHeader().setHighlightSections(True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_5.setGeometry(QtCore.QRect(390, 530, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tableWidget_5.setFont(font)
        self.tableWidget_5.setAutoFillBackground(False)
        self.tableWidget_5.setStyleSheet("QTableWidget {\n"
"        color: rgb(4, 192, 157);\n"
"    outline: none;\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"    }\n"
"QTableWidget::item:selected {\n"
"    background-color: transparent;\n"
"    color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:selected QLineEdit {\n"
"  color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:focus {\n"
"        border: none;\n"
"    }\n"
"QLineEdit:focus {\n"
"    border: none;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: transparent;\n"
"    color: rgb(147, 147, 147);\n"
"}")
        self.tableWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_5.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_5.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_5.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_5.setRowCount(11)
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setObjectName("tableWidget_5")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(10, item)
        self.tableWidget_5.horizontalHeader().setVisible(False)
        self.tableWidget_5.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(37)
        self.tableWidget_5.horizontalHeader().setHighlightSections(True)
        self.tableWidget_5.verticalHeader().setVisible(True)
        self.tableWidget_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_5.verticalHeader().setHighlightSections(True)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(740, 530, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tableWidget_6.setFont(font)
        self.tableWidget_6.setAutoFillBackground(False)
        self.tableWidget_6.setStyleSheet("QTableWidget {\n"
"        color: rgb(4, 192, 157);\n"
"    outline: none;\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"    }\n"
"QTableWidget::item:selected {\n"
"    background-color: transparent;\n"
"    color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:selected QLineEdit {\n"
"  color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:focus {\n"
"        border: none;\n"
"    }\n"
"QLineEdit:focus {\n"
"    border: none;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: transparent;\n"
"    color: rgb(147, 147, 147);\n"
"}")
        self.tableWidget_6.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_6.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_6.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_6.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.setColumnCount(3)
        self.tableWidget_6.setObjectName("tableWidget_6")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        self.tableWidget_6.horizontalHeader().setVisible(True)
        self.tableWidget_6.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(37)
        self.tableWidget_6.horizontalHeader().setHighlightSections(True)
        self.tableWidget_6.verticalHeader().setVisible(False)
        self.tableWidget_6.verticalHeader().setCascadingSectionResizes(False)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1200, 95, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(147, 147, 147);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 500, 181, 16))
        self.label_4.setStyleSheet("color: rgb(147, 147, 147);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(750, 500, 181, 16))
        self.label_5.setStyleSheet("color: rgb(147, 147, 147);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1090, 500, 181, 16))
        self.label_6.setStyleSheet("color: rgb(147, 147, 147);")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 51, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(4, 192, 157);\n"
"selection-background-color:  transparent;\n"
"selection-color: rgb(147, 147, 147);\n"
"border: 2px solid rgb(147, 147, 147) ;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_7.setGeometry(QtCore.QRect(1080, 530, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tableWidget_7.setFont(font)
        self.tableWidget_7.setAutoFillBackground(False)
        self.tableWidget_7.setStyleSheet("QTableWidget {\n"
"        color: rgb(4, 192, 157);\n"
"    outline: none;\n"
"    border: 2px solid rgb(147, 147, 147);\n"
"    }\n"
"QTableWidget::item:selected {\n"
"    background-color: transparent;\n"
"    color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:selected QLineEdit {\n"
"  color: rgb(147, 147, 147);\n"
"}\n"
"QTableWidget::item:focus {\n"
"        border: none;\n"
"    }\n"
"QLineEdit:focus {\n"
"    border: none;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: transparent;\n"
"    color: rgb(147, 147, 147);\n"
"}")
        self.tableWidget_7.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_7.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_7.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_7.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.setColumnCount(2)
        self.tableWidget_7.setObjectName("tableWidget_7")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        self.tableWidget_7.horizontalHeader().setVisible(True)
        self.tableWidget_7.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_7.horizontalHeader().setDefaultSectionSize(37)
        self.tableWidget_7.horizontalHeader().setHighlightSections(True)
        self.tableWidget_7.verticalHeader().setVisible(False)
        self.tableWidget_7.verticalHeader().setCascadingSectionResizes(False)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(110, 740, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.radioButton_3.setFont(font)
        self.radioButton_3.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.radioButton_3.setStyleSheet("QRadioButton {\n"
"    color: rgb(147, 147, 147);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"    border-radius: 25px;\n"
"    width: 50px;\n"
"    height: 50px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"    border-radius: 25px;\n"
"    width: 50px;\n"
"    height: 50px;\n"
"}\n"
"")
        self.radioButton_3.setText("")
        self.radioButton_3.setIconSize(QtCore.QSize(20, 20))
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 740, 41, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(44)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(147, 147, 147);")
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 530, 301, 191))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: rgb(4, 192, 157);\n"
"selection-background-color:  transparent;\n"
"selection-color: rgb(147, 147, 147);\n"
"border: 2px solid rgb(147, 147, 147) ;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 430, 301, 101))
        self.textBrowser_2.setStyleSheet("color: rgb(4, 192, 157);\n"
"selection-background-color:  transparent;\n"
"selection-color: rgb(147, 147, 147);\n"
"border: 2px solid rgb(147, 147, 147) ;\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.tableWidget.raise_()
        self.spinBox.raise_()
        self.spinBox_2.raise_()
        self.tableWidget_2.raise_()
        self.tableWidget_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tableWidget_4.raise_()
        self.tableWidget_5.raise_()
        self.tableWidget_6.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.lineEdit.raise_()
        self.tableWidget_7.raise_()
        self.radioButton_3.raise_()
        self.label_7.raise_()
        self.textBrowser.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Порождающая матрица G"))
        self.radioButton_2.setText(_translate("MainWindow", "Проверочная матрица H"))
        self.label.setText(_translate("MainWindow", "Gsys"))
        self.label_2.setText(_translate("MainWindow", "Hsys"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "n"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "k"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "dmin"))
        item = self.tableWidget_5.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "t"))
        item = self.tableWidget_5.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "p"))
        item = self.tableWidget_5.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Исходный текст"))
        item = self.tableWidget_5.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Бинарный вид"))
        item = self.tableWidget_5.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Код"))
        item = self.tableWidget_5.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Код с ошибками"))
        item = self.tableWidget_5.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Декод"))
        item = self.tableWidget_5.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Полученный текст"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "i"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "c"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Wh"))
        self.label_3.setText(_translate("MainWindow", "HsysT"))
        self.label_4.setText(_translate("MainWindow", "Числовые характеристики"))
        self.label_5.setText(_translate("MainWindow", "Таблица кодовых слов"))
        self.label_6.setText(_translate("MainWindow", "Таблица синдромов"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "e"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "S"))
        self.label_7.setText(_translate("MainWindow", "?"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">&quot;Теория информации и истичники кодирования&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"></span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
