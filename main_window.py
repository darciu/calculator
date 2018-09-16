from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class mainWindow(QMainWindow):

    operators = ['+','-','*','/','** 2','** 0.5']
    operation_list = []

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(400,200,200,200)

        self.create_main_layout()
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.main_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)


    @classmethod
    def operation_list_append(cls, value):
        cls.operation_list.append(value)

    @classmethod
    def operation_list_remove_last(cls):
        cls.operation_list.pop()

    @classmethod
    def operation_list_clear(cls):
        cls.operation_list = []


    def create_main_layout(self):


        #self.main_layout = QVBoxLayout()


        self.display = QLineEdit()
        self.display_formula = QLineEdit()

        #buttons

        self.button_0 = QPushButton('0')
        self.button_1 = QPushButton('1')
        self.button_2 = QPushButton('2')
        self.button_3 = QPushButton('3')
        self.button_4 = QPushButton('4')
        self.button_5 = QPushButton('5')
        self.button_6 = QPushButton('6')
        self.button_7 = QPushButton('7')
        self.button_8 = QPushButton('8')
        self.button_9 = QPushButton('9')
        self.button_comma = QPushButton('.')
        self.button_plus = QPushButton('+')
        self.button_minus = QPushButton('-')
        self.button_multiply = QPushButton('*')
        self.button_divide = QPushButton('/')
        self.button_equals = QPushButton('=')
        self.button_sqrt = QPushButton('SQRT')
        self.button_power = QPushButton('^2')
        self.button_lbracket = QPushButton('(')
        self.button_rbracket = QPushButton(')')
        self.button_clear = QPushButton('C')
        self.button_clear_recent = QPushButton('<-')

        #grids

        self.buttons_grid = QGridLayout()
        self.operators_grid = QGridLayout()
        self.clear_grid = QGridLayout()
        self.displays_grid = QGridLayout()
        self.main_grid = QGridLayout()

        #buttons connections

        self.button_0.clicked.connect(self.click_button_0)
        self.button_1.clicked.connect(self.click_button_1)
        self.button_2.clicked.connect(self.click_button_2)
        self.button_3.clicked.connect(self.click_button_3)
        self.button_4.clicked.connect(self.click_button_4)
        self.button_5.clicked.connect(self.click_button_5)
        self.button_6.clicked.connect(self.click_button_6)
        self.button_7.clicked.connect(self.click_button_7)
        self.button_8.clicked.connect(self.click_button_8)
        self.button_9.clicked.connect(self.click_button_9)
        self.button_comma.clicked.connect(self.click_button_comma)
        self.button_clear.clicked.connect(self.click_button_clear)
        self.button_clear_recent.clicked.connect(self.click_button_clear_recent)
        self.button_plus.clicked.connect(self.click_button_plus)
        self.button_minus.clicked.connect(self.click_button_minus)
        self.button_multiply.clicked.connect(self.click_button_multiply)
        self.button_divide.clicked.connect(self.click_button_divide)
        self.button_sqrt.clicked.connect(self.click_button_sqrt)
        self.button_power.clicked.connect(self.click_button_power)
        self.button_lbracket.clicked.connect(self.click_button_lbracket)
        self.button_rbracket.clicked.connect(self.click_button_rbracket)
        self.button_equals.clicked.connect(self.click_button_equals)


        #build grids

        self.buttons_grid.addWidget(self.button_7,0,0)
        self.buttons_grid.addWidget(self.button_8, 0, 1)
        self.buttons_grid.addWidget(self.button_9, 0, 2)
        self.buttons_grid.addWidget(self.button_4, 1, 0)
        self.buttons_grid.addWidget(self.button_5, 1, 1)
        self.buttons_grid.addWidget(self.button_6, 1, 2)
        self.buttons_grid.addWidget(self.button_1, 2, 0)
        self.buttons_grid.addWidget(self.button_2, 2, 1)
        self.buttons_grid.addWidget(self.button_3, 2, 2)
        self.buttons_grid.addWidget(self.button_0, 3, 0)
        self.buttons_grid.addWidget(self.button_comma, 3, 1)
        self.buttons_grid.addWidget(self.button_equals, 3, 2)

        self.operators_grid.addWidget(self.button_plus,0,0)
        self.operators_grid.addWidget(self.button_minus, 1, 0)
        self.operators_grid.addWidget(self.button_multiply, 2, 0)
        self.operators_grid.addWidget(self.button_divide, 3, 0)
        self.operators_grid.addWidget(self.button_sqrt,0,1)
        self.operators_grid.addWidget(self.button_power, 1, 1)
        self.operators_grid.addWidget(self.button_lbracket, 2, 1)
        self.operators_grid.addWidget(self.button_rbracket, 3, 1)

        self.displays_grid.addWidget(self.display_formula, 0, 0)
        self.displays_grid.addWidget(self.display,1,0)

        self.clear_grid.addWidget(self.button_clear,0,0)
        self.clear_grid.addWidget(self.button_clear_recent, 1, 0)

        self.main_grid.addLayout(self.displays_grid,0,0)
        self.main_grid.addLayout(self.clear_grid,0,1)
        self.main_grid.addLayout(self.buttons_grid,1,0)
        self.main_grid.addLayout(self.operators_grid, 1, 1)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_grid)


    def click_button_0(self):
        if self.display.text() == '' or '.' in self.display.text() or self.display.text()[0] in ['1','2','3','4','5','6','7','8','9']:
            self.display.setText(self.display.text() + '0')

    def click_button_1(self):
        self.display.setText(self.display.text() + '1')

    def click_button_2(self):
        self.display.setText(self.display.text() + '2')

    def click_button_3(self):
        self.display.setText(self.display.text() + '3')

    def click_button_4(self):
        self.display.setText(self.display.text() + '4')

    def click_button_5(self):
        self.display.setText(self.display.text() + '5')

    def click_button_6(self):
        self.display.setText(self.display.text() + '6')

    def click_button_7(self):
        self.display.setText(self.display.text() + '7')

    def click_button_8(self):
        self.display.setText(self.display.text() + '8')

    def click_button_9(self):
        self.display.setText(self.display.text() + '9')

    def click_button_comma(self):
        if '.' not in self.display.text():
            if len(self.display.text()) == 0:
                self.display.setText('0.')
            else:
                self.display.setText(self.display.text() + '.')

    def click_button_clear(self):
        self.display.setText('')
        self.display_formula.setText('')
        self.operation_list_clear()

    def click_button_clear_recent(self):
        if len(self.operation_list) > 0:
            self.operation_list_remove_last()
            self.display_formula.setText(" ".join(self.operation_list))

    def click_button_plus(self):
        self.append_number()

        if len(self.operation_list) > 0:
            if self.operation_list[-1] not in self.operators:
                self.operation_list_append('+')

        self.display_formula.setText(" ".join(self.operation_list))

    def click_button_minus(self):
        self.append_number()

        if len(self.operation_list) > 0:
            if self.operation_list[-1] not in self.operators:
                self.operation_list_append('-')

        self.display_formula.setText(" ".join(self.operation_list))

    def click_button_multiply(self):
        self.append_number()

        if len(self.operation_list) > 0:
            if self.operation_list[-1] not in self.operators:
                self.operation_list_append('*')

        self.display_formula.setText(" ".join(self.operation_list))

    def click_button_divide(self):
        self.append_number()

        if len(self.operation_list) > 0:
            if self.operation_list[-1] not in self.operators:
                self.operation_list_append('/')

        self.display_formula.setText(" ".join(self.operation_list))

    def click_button_sqrt(self):
        self.append_number()

        if len(self.operation_list) > 0:
            if self.operation_list[-1] not in self.operators:
                self.operation_list_append('** 0.5')

        self.display_formula.setText(" ".join(self.operation_list))


    def click_button_power(self):
        self.append_number()

        if len(self.operation_list) > 0:
            if self.operation_list[-1] not in self.operators:
                self.operation_list_append('** 2')

        self.display_formula.setText(" ".join(self.operation_list))

    def click_button_lbracket(self):
        self.append_number()

        if len(self.operation_list) > 0:
            if self.operation_list[-1] != ')' and self.operation_list[-1] not in '0123456789':
                self.operation_list_append('(')
        else:
            self.operation_list_append('(')
        self.display_formula.setText(" ".join(self.operation_list))

    def click_button_rbracket(self):
        self.append_number()
        if self.operation_list.count(')') < self.operation_list.count('('):
            if len(self.operation_list) > 1:
                if self.operation_list[-1] != '(' and self.operation_list[-1] not in self.operators:
                    self.operation_list_append(')')

        self.display_formula.setText(" ".join(self.operation_list))

    def click_button_equals(self):

        if self.check_formula():
            try:
                self.display_formula.setText(" ".join(self.operation_list) + " " + self.display.text() + " =")
                self.display.setText(str(eval(" ".join(self.operation_list) + " " + self.display.text())))
                self.operation_list_clear()
            except ZeroDivisionError:
                self.operation_list_clear()
        else:
            print('oky')


    def append_number(self):
        if self.display.text() != '':
            self.operation_list_append(self.display.text())
            self.display.setText('')

    def check_formula(self):
        if self.operation_list.count('(') == self.operation_list.count(')'):
            return True









def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    window.raise_()
    app.exec()

if __name__ == '__main__':
    main()