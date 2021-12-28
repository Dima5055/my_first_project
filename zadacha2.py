# -*- coding: utf-8 -*-
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from maybework import Ui_MainWindow


def toBASE(number, base_in):
    b = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = b[number % base_in]
    while number >= base_in:
        number //= base_in
        a += b[number % base_in]
    return a[::-1]


def proverka(number, base_in):
    f = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k = 0
    for i in number:
        if i in f[0:int(base_in)]:
            k += 1
    return k


def nine_or_eleven(what_clas, cur):
    issue_numbers = []
    if what_clas == "11 класс":
        result = cur.execute("""SELECT id FROM ege""").fetchall()
        for i in result:
            issue_numbers.append(str(i[0]))
    elif what_clas == "9 класс":
        result = cur.execute("""SELECT id FROM oge""").fetchall()
        for i in result:
            issue_numbers.append(str(i[0]))
    return issue_numbers


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Системы счисления')
        self.button_perevod.clicked.connect(self.go)
        self.button_sum.clicked.connect(self.sum)
        self.button_minus.clicked.connect(self.minus)
        self.button_pro.clicked.connect(self.pro)
        self.what_clas.addItem("9 класс")
        self.what_clas.addItem("11 класс")
        self.button_go.clicked.connect(self.go_task)
        self.respond.clicked.connect(self.to_respond)
        self.respond.setEnabled(False)

    def go(self):
        translate_number = str(self.translate_number.text())
        base = str(self.base.text())
        new_base = str(self.new_base.text())
        if translate_number == "" or base == "" or new_base == "":
            self.label_yes_or_no.setText("Заполните все элементы!")

        elif int(base) > 36 or int(new_base) > 36:
            self.label_yes_or_no.setText("Система счисления не может быть больше 36!")

        else:
            k = proverka(translate_number, base)
            if len(translate_number) != k:
                self.label_yes_or_no.setFont(('Arial', 7))
                self.label_yes_or_no.setText("Введите коректные данные! Можно использовать числа, от 1 до 9 "
                                             "и заглавные буквы\n"
                                             "латинского алфавита. И не забудьте, что в числе не может "
                                             "быть цифр больше основания ")
                self.translate_number.clear()
            elif len(translate_number) == k:
                self.label_yes_or_no.clear()
                number_in_10 = int(translate_number, int(base))
                new_number = toBASE(number_in_10, int(new_base))
                self.new_number.setText(str(new_number))

    def sum(self):
        self.three_number.clear()
        first_number = str(self.first_number.text())
        first_base = str(self.first_base.text())
        second_number = str(self.second_number.text())
        second_base = str(self.second_base.text())
        three_base = str(self.three_base.text())
        k1 = proverka(first_number, first_base)
        k2 = proverka(second_number, second_base)
        if ((first_number == "" or first_base == "" or second_number == "" or second_base == "" or three_base == "")
                or (int(first_base) > 36 or int(second_base) > 36 or int(three_base) > 36)):
            if first_number == "" or first_base == "" or second_number == "" or second_base == "" or three_base == "":
                self.label_yes_or_no_2.setText("Заполните все элементы!")

            elif int(first_base) > 36 or int(second_base) > 36 or int(three_base) > 36:
                self.label_yes_or_no_2.setText("Система счисления не может быть больше 36!")

        else:
            if k1 != len(first_number):
                self.label_yes_or_no_2.setFont(('Arial', 7))
                self.label_yes_or_no_2.setText("Проверьте ваше первое число на корректность!")
            elif k2 != len(second_number):
                self.label_yes_or_no_2.setFont(('Arial', 7))
                self.label_yes_or_no_2.setText("Проверьте ваше второе число на корректность!")
            else:
                self.label_yes_or_no_2.clear()
                number_in_10_1 = int(first_number, int(first_base))
                number_in_10_2 = int(second_number, int(second_base))
                new = number_in_10_1 + number_in_10_2
                new_number = toBASE(new, int(three_base))
                self.three_number.setText(str(new_number))

    def minus(self):
        first_number = str(self.first_number.text())
        first_base = str(self.first_base.text())
        second_number = str(self.second_number.text())
        second_base = str(self.second_base.text())
        three_base = str(self.three_base.text())
        k1 = proverka(first_number, first_base)
        k2 = proverka(second_number, second_base)
        if ((first_number == "" or first_base == "" or second_number == "" or second_base == "" or three_base == "")
                or (int(first_base) > 36 or int(second_base) > 36 or int(three_base) > 36)):
            if first_number == "" or first_base == "" or second_number == "" or second_base == "" or three_base == "":
                self.label_yes_or_no_2.setText("Заполните все элементы!")

            elif int(first_base) > 36 or int(second_base) > 36 or int(three_base) > 36:
                self.label_yes_or_no_2.setText("Система счисления не может быть больше 36!")

        else:
            if k1 != len(first_number):
                self.label_yes_or_no_2.setFont(('Arial', 7))
                self.label_yes_or_no_2.setText("Проверьте ваше первое число на корректность!")
            elif k2 != len(second_number):
                self.label_yes_or_no_2.setFont(('Arial', 7))
                self.label_yes_or_no_2.setText("Проверьте ваше второе число на корректность!")
            else:
                self.label_yes_or_no_2.clear()
                number_in_10_1 = int(first_number, int(first_base))
                number_in_10_2 = int(second_number, int(second_base))
                new = number_in_10_1 - number_in_10_2
                new_number = toBASE(new, int(three_base))
                self.three_number.setText(str(new_number))

    def pro(self):
        first_number = str(self.first_number.text())
        first_base = str(self.first_base.text())
        second_number = str(self.second_number.text())
        second_base = str(self.second_base.text())
        three_base = str(self.three_base.text())
        k1 = proverka(first_number, first_base)
        k2 = proverka(second_number, second_base)
        if ((first_number == "" or first_base == "" or second_number == "" or second_base == "" or three_base == "")
                or (int(first_base) > 36 or int(second_base) > 36 or int(three_base) > 36)):
            if first_number == "" or first_base == "" or second_number == "" or second_base == "" or three_base == "":
                self.label_yes_or_no_2.setText("Заполните все элементы!")

            elif int(first_base) > 36 or int(second_base) > 36 or int(three_base) > 36:
                self.label_yes_or_no_2.setText("Система счисления не может быть больше 36!")

        else:
            if k1 != len(first_number):
                self.label_yes_or_no_2.setFont(('Arial', 7))
                self.label_yes_or_no_2.setText("Проверьте ваше первое число на корректность!")
            elif k2 != len(second_number):
                self.label_yes_or_no_2.setFont(('Arial', 7))
                self.label_yes_or_no_2.setText("Проверьте ваше второе число на корректность!")
            else:
                self.label_yes_or_no_2.clear()
                number_in_10_1 = int(first_number, int(first_base))
                number_in_10_2 = int(second_number, int(second_base))
                new = number_in_10_1 * number_in_10_2
                new_number = toBASE(new, int(three_base))
                self.three_number.setText(str(new_number))

    def go_task(self):
        task = str(self.task.text())
        self.my_list.clear()
        what_clas = str(self.what_clas.currentText())
        con = sqlite3.connect("my_database")
        cur = con.cursor()
        issue_numbers = nine_or_eleven(what_clas, cur)
        if task == "":
            self.label_comment.setText("Выберете задачу!")
        else:
            if task not in issue_numbers:
                self.label_comment.setText("К сожаление данной задачи нет.")
                self.new_answer.clear()
            else:
                self.label_comment.clear()
                if what_clas == "11 класс":
                    file = task + ".11.txt"
                    f = open(file, encoding="utf-8")
                    for i in f:
                        self.my_list.addItem(str(i))
                else:
                    file = task + ".9.txt"
                    f = open(file, encoding="utf-8")
                    for i in f:
                        self.my_list.addItem(str(i))
                self.respond.setEnabled(True)

    def to_respond(self):
        task = str(self.task.text())
        new_answer = str(self.new_answer.text())
        self.label_comment.clear()
        what_clas = str(self.what_clas.currentText())
        con = sqlite3.connect("my_database")
        cur = con.cursor()
        f = nine_or_eleven(what_clas, cur)
        if task in f:
            if what_clas == "11 класс":
                result = cur.execute("""SELECT answer FROM ege
                         WHERE id = ?""", task).fetchall()
                if new_answer == str(result[0][0]):
                    self.label_comment.setText("Правильный ответ!")
                else:
                    self.label_comment.setText("К сожаление, не правильный ответ!")
            else:
                result = cur.execute("""SELECT answer FROM oge
                                 WHERE id = ?""", task).fetchall()
                if new_answer == str(result[0][0]):
                    self.label_comment.setText("Правильный ответ!")
                else:
                    self.label_comment.setText("К сожаление, не правильный ответ!")
        else:
            self.label_comment.setText("Пожалуйста, введите корректно номер задачи!")
            self.respond.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setStyleSheet(
        "#MainWindow{border-image:url(background.jpg)}")
    ex.show()
    sys.exit(app.exec_())
