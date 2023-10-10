import sys
import numpy as np
import itertools
import random
from PyQt5 import QtWidgets
from interface import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
class Coding(QtWidgets.QMainWindow):
    def __init__(self):
        super(Coding, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.spinBoxMValue = 0
        self.spinBoxNValue = 0
        self.them = 0

    def init_UI(self):
        self.setWindowTitle('Матричное представление блочных кодов')
        self.ui.spinBox.valueChanged.connect(self.spinBoxMEdit)
        self.ui.spinBox_2.valueChanged.connect(self.spinBoxNEdit)
        self.ui.tableWidget.cellClicked.connect(self.cellClicked)
        self.ui.radioButton.clicked.connect(self.start)
        self.ui.radioButton_2.clicked.connect(self.start)
        self.ui.lineEdit.textChanged.connect(self.onTextChanged)
        self.ui.radioButton_3.clicked.connect(self.change_them)
        self.ui.label_7.enterEvent = self.faq_in
        self.ui.label_7.leaveEvent = self.faq_out
        self.ui.textBrowser.hide()

    def faq_in(self, event):
        self.ui.textBrowser.show()

    def faq_out(self, event):
        self.ui.textBrowser.hide()

    def change_them(self):
        if self.them == 0:
            self.ui.radioButton_3.setStyleSheet("QRadioButton {\n"
 "    color: rgb(147, 147, 147);\n"
 "}\n"
 "\n"
 "QRadioButton::indicator:checked {\n"
 "    border: 3px solid rgb(47, 47, 47);\n"
 "    border-radius: 25px;\n"
 "    width: 50px;\n"
 "    height: 50px;\n"
 "}\n"
 "\n"
 "QRadioButton::indicator {\n"
 "    border: 3px solid rgb(47, 47, 47);\n"
 "    border-radius: 25px;\n"
 "    width: 50px;\n"
 "    height: 50px;\n"
 "}\n"
 "")
            self.setStyleSheet("QMainWindow, QWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
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
            self.them = 1
        else:
            self.ui.radioButton_3.setStyleSheet("QRadioButton {\n"
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
            self.setStyleSheet("QMainWindow, QWidget {\n"
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
            self.them = 0

    def onTextChanged(self):
        self.ui.radioButton.setAutoExclusive(False)
        self.ui.radioButton_2.setAutoExclusive(False)
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton.setAutoExclusive(True)
        self.ui.radioButton_2.setAutoExclusive(True)

    def spinBoxMEdit(self, new_value):
        self.ui.radioButton.setAutoExclusive(False)
        self.ui.radioButton_2.setAutoExclusive(False)
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton.setAutoExclusive(True)
        self.ui.radioButton_2.setAutoExclusive(True)
        if new_value < self.spinBoxMValue:
            self.ui.tableWidget.setRowCount(new_value)
        elif new_value > self.spinBoxMValue:
            self.ui.tableWidget.setRowCount(new_value)
            for j in range(self.spinBoxMValue, new_value):
                for i in range(self.spinBoxNValue):
                    cell = QTableWidgetItem("0")
                    cell.setTextAlignment(Qt.AlignCenter)
                    self.ui.tableWidget.setItem(j, i, cell)
        self.spinBoxMValue = new_value

    def spinBoxNEdit(self, new_value):
        self.ui.radioButton.setAutoExclusive(False)
        self.ui.radioButton_2.setAutoExclusive(False)
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton.setAutoExclusive(True)
        self.ui.radioButton_2.setAutoExclusive(True)
        if new_value < self.spinBoxNValue:
            self.ui.tableWidget.setColumnCount(new_value)
        elif new_value > self.spinBoxNValue:
            self.ui.tableWidget.setColumnCount(new_value)
            for j in range(self.spinBoxNValue, new_value):
                for i in range(self.spinBoxMValue):
                    cell = QTableWidgetItem("0")
                    cell.setTextAlignment(Qt.AlignCenter)
                    self.ui.tableWidget.setItem(i, j, cell)
        self.spinBoxNValue = new_value

    def cellClicked(self, row, col):
        self.ui.radioButton.setAutoExclusive(False)
        self.ui.radioButton_2.setAutoExclusive(False)
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton.setAutoExclusive(True)
        self.ui.radioButton_2.setAutoExclusive(True)
        value = self.ui.tableWidget.item(row, col).text()
        cell = QTableWidgetItem(str(int(not(int(value)))))
        cell.setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.setItem(row, col, cell)

    def start(self):
        if self.ui.radioButton.isChecked():
            Gm = self.spinBoxMValue
            Gn = self.spinBoxNValue
            G = self.input_matrix(Gm, Gn)
            Gsys = self.G2Gsys(G, Gm, Gn)
            self.print_matrix(self.ui.tableWidget_2, Gsys, Gm, Gn)
            Hsys = self.Gsys2Hsys(Gsys, Gm, Gn)
            Hm = Gn - Gm
            Hn = Gn
            self.print_matrix(self.ui.tableWidget_3, Hsys, Hm, Hn)
        else:
            Hm = self.spinBoxMValue
            Hn = self.spinBoxNValue
            H = self.input_matrix(Hm, Hn)
            Hsys = self.H2Hsys(H, Hm, Hn)
            self.print_matrix(self.ui.tableWidget_3, Hsys, Hm, Hn)
            Gsys = self.Hsys2Gsys(Hsys, Hm, Hn)
            Gm = Hn - Hm
            Gn = Hn
            self.print_matrix(self.ui.tableWidget_2, Gsys, Gm, Gn)
        n = Gn
        k = Gm
        code_word_table = self.Gsys2Code_word_table(Gsys, k)
        Wh = self.print_code_word_table(code_word_table)
        dmin = min(Wh[1:])
        t = int((dmin - 1) / 2)
        p = dmin - 1
        text = self.ui.lineEdit.text()
        binary, zeros = self.text2binary(text, k)
        binary_code = self.Binary2Binary_code(binary, code_word_table, k)
        Vbinary_code = self.Binary_code2VBinary_code(binary_code, n, t)
        HsysT = Hsys.transpose()
        self.print_matrix(self.ui.tableWidget_4, HsysT, Hn, Hm)
        syndrome_table = self.HsysT2Syndrome_table(HsysT, n, t)
        self.print_syndrome_table(syndrome_table)
        binary_decode = self.Binary_code2Binary(Vbinary_code, HsysT, syndrome_table, code_word_table, n)
        text_decode = self.Binary_decode2Text_decode(binary_decode, zeros)
        self.characteristics(n, k, dmin, t, p, text, binary, binary_code, Vbinary_code, binary_decode, text_decode)

    def input_matrix(self, m, n):
        matrix = np.zeros((m, n), dtype=int)
        for i in range(m):
            for j in range(n):
                matrix[i, j] = int(self.ui.tableWidget.item(i, j).text())
        return matrix

    def print_matrix(self, table, matrix, m, n):
        table.setRowCount(m)
        table.setColumnCount(n)
        for i in range(m):
            for j in range(n):
                cell = QTableWidgetItem(str(matrix[i, j]))
                cell.setTextAlignment(Qt.AlignCenter)
                table.setItem(i, j, cell)

    def G2Gsys(self, G, Gm, Gn):
        Gsys = np.copy(G)
        for i in range(Gm):
            for j in range(i + 1, Gn):
                if np.sum(Gsys[:, j]) == 1 and Gsys[i, j] == 1:
                    temp = np.copy(Gsys[:, j])
                    Gsys[:, j] = Gsys[:, i]
                    Gsys[:, i] = temp
        return Gsys

    def H2Hsys(self, H, Hm, Hn):
        Hsys = np.copy(H)
        for i in range(Hm):
            for j in range(Hn - 1 - i):
                if np.sum(Hsys[:, j]) == 1 and Hsys[Hm - 1 - i, j] == 1:
                    temp = np.copy(Hsys[:, j])
                    Hsys[:, j] = Hsys[:, Hn - 1 - i]
                    Hsys[:, Hn - 1 - i] = temp
        return Hsys

    def Gsys2Hsys(self, Gsys, Gm, Gn):
        return np.hstack([Gsys[:, Gm:].transpose(), np.eye(Gn - Gm, dtype=int)])

    def Hsys2Gsys(self, Hsys, Hm, Hn):
        return np.hstack([np.eye(Hn - Hm, dtype=int), Hsys[:, :Hn - Hm].transpose()])

    def characteristics(self, n, k, dmin, t, p, text, binary, binary_code, Vbinary_code, binary_decode, text_decode):
        cell = QTableWidgetItem(str(n))
        self.ui.tableWidget_5.setItem(0, 0, cell)
        cell = QTableWidgetItem(str(k))
        self.ui.tableWidget_5.setItem(1, 0, cell)
        cell = QTableWidgetItem(str(dmin))
        self.ui.tableWidget_5.setItem(2, 0, cell)
        cell = QTableWidgetItem(str(t))
        self.ui.tableWidget_5.setItem(3, 0, cell)
        cell = QTableWidgetItem(str(p))
        self.ui.tableWidget_5.setItem(4, 0, cell)
        cell = QTableWidgetItem(text)
        self.ui.tableWidget_5.setItem(5, 0, cell)
        cell = QTableWidgetItem(binary)
        self.ui.tableWidget_5.setItem(6, 0, cell)
        cell = QTableWidgetItem(''.join(map(str, binary_code)))
        self.ui.tableWidget_5.setItem(7, 0, cell)
        cell = QTableWidgetItem(''.join(map(str, Vbinary_code)))
        self.ui.tableWidget_5.setItem(8, 0, cell)
        cell = QTableWidgetItem(binary_decode)
        self.ui.tableWidget_5.setItem(9, 0, cell)
        cell = QTableWidgetItem(text_decode)
        self.ui.tableWidget_5.setItem(10, 0, cell)
        self.ui.tableWidget_5.resizeColumnsToContents()

    def Gsys2Code_word_table(self, Gsys, k):
        code_word_table = {}
        for i in list(itertools.product([0, 1], repeat=k)):
            code_word_table[''.join(map(str, i))] = np.mod(np.dot(Gsys.transpose(), i), 2)
        return code_word_table

    def print_code_word_table(self,code_word_table):
        self.ui.tableWidget_6.setRowCount(len(code_word_table))
        Wh = []
        j = 0
        for i in code_word_table.items():
            Wh.append(np.sum(i[1]))
            cell = QTableWidgetItem(i[0])
            cell.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_6.setItem(j, 0, cell)
            cell = QTableWidgetItem(''.join(map(str, i[1])))
            cell.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_6.setItem(j, 1, cell)
            cell = QTableWidgetItem(str(np.sum(i[1])))
            cell.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_6.setItem(j, 2, cell)
            self.ui.tableWidget_6.resizeColumnsToContents()
            j = j + 1
        return Wh

    def text2binary(self, text, k):
        binary = ''.join(["0" * (14 - len(str(bin(ord(i))[2:]))) + str(bin(ord(i))[2:]) for i in text])
        zeros = 0
        if len(binary) % k != 0:
            zeros = k - (len(binary) % k)
            binary = "0" * zeros + binary
        return binary, zeros

    def Binary2Binary_code(self, binary, code_word_table, k):
        binary_code = np.array([], dtype=int)
        for i in range(0, len(binary), k):
            binary_code = np.hstack([binary_code, code_word_table[binary[i:i + k]]])
        return binary_code

    def Binary_code2VBinary_code(self, binary_code, n, t):
        Vbinary_code = binary_code.copy()
        for i in range(0, len(binary_code), n):
            mistakes = random.sample(range(n), t)
            for x in mistakes:
                Vbinary_code[i + x] = not (Vbinary_code[i + x])
        return Vbinary_code

    def HsysT2Syndrome_table(self, HsysT, n, t):
        syndrome_table = {}
        vector = np.zeros(n, dtype=int)
        for i in range(t):
            vector[i] = 1
        for e in sorted(set(itertools.permutations(vector))):
            syndrome_table[''.join(map(str, np.mod(np.dot(HsysT.transpose(), e), 2)))] = e
        return syndrome_table

    def print_syndrome_table(self, syndrome_table):
        self.ui.tableWidget_7.setRowCount(len(syndrome_table))
        j = 0
        for i in syndrome_table.items():
            cell = QTableWidgetItem(''.join(map(str, i[1])))
            cell.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_7.setItem(j, 0, cell)
            cell = QTableWidgetItem(i[0])
            cell.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget_7.setItem(j, 1, cell)
            self.ui.tableWidget_7.resizeColumnsToContents()
            j = j + 1

    def Binary_code2Binary(self, Vbinary_code, HsysT, syndrome_table, code_word_table, n):
        binary_decode = ""
        for i in range(0, len(Vbinary_code), n):
            v = Vbinary_code[i:i + n]
            S = np.mod(np.dot(HsysT.transpose(), v), 2)
            e = syndrome_table[''.join(map(str, S))]
            c = (v + e) % 2
            for j in code_word_table.items():
                if np.array_equal(j[1], c):
                    binary_decode += j[0]
        return binary_decode

    def Binary_decode2Text_decode(self, binary_decode, zeros):
        return ''.join([chr(int(binary_decode[i:i + 14], 2)) for i in range(zeros, len(binary_decode), 14)])

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Coding()
    application.show()
    sys.exit(app.exec())