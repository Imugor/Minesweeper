from PyQt5 import Qt, QtCore, QtWidgets, QtGui
from SaperClass import Saper
import sys
import os

os.system('pyuic5 saper.ui -o MainWindow.py')
from MainWindow import Ui_MainWindow


class CellButton(Qt.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mine = False
        self.hide = True

    def mousePressEvent(self, event):
        button = event.button()
        if button == Qt.Qt.RightButton:
            if not self.hide:
                return Qt.QPushButton.mousePressEvent(self, event)
            if not self.mine:
                self.setStyleSheet("""background-color: rgb(0, 0, 255);""")
                self.mine = True
            else:
                self.setStyleSheet("""background-color: rgb(213, 213, 213);""")
                self.mine = False

        return Qt.QPushButton.mousePressEvent(self, event)


class MyWindow(QtWidgets.QMainWindow):
    size_button = 50
    padding = 10
    height_up_layout = 30

    def __init__(self):
        super(MyWindow, self).__init__()

        self.time_sec = None
        self.timer = None
        self.button = None
        self.saper_game = None
        self.buttons = None
        self.height = None
        self.width = None
        self.n_but_vertical = 5
        self.n_but_horizont = 5
        self.n_mines = 5

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.restart_game())
        self.ui.act_easy.triggered.connect(lambda: self.set_difficulty(0))
        self.ui.act_mid.triggered.connect(lambda: self.set_difficulty(1))
        self.ui.act_hard.triggered.connect(lambda: self.set_difficulty(2))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.thread_second)
        self.timer.start(1000)
        self.create_window()

    def thread_second(self):
        self.time_sec += 1
        self.ui.label_time.setText(str(self.time_sec))

    def set_difficulty(self, dif):
        dif_arr = [(5, 5, 5), (10, 10, 20), (15, 15, 60)]
        self.restart_game(dif_arr[dif][0], dif_arr[dif][1], dif_arr[dif][2])

    def set_n_cells_mines(self, n_but_horizont=None, n_but_vertical=None, n_mines=None):
        self.n_but_horizont = n_but_horizont if n_but_horizont is not None else self.n_but_horizont
        self.n_but_vertical = n_but_vertical if n_but_vertical is not None else self.n_but_vertical
        self.n_mines = n_mines if n_mines is not None else self.n_mines

    def create_window(self):
        self.width = self.padding * 2 + self.n_but_horizont * self.size_button
        self.height = self.height_up_layout + self.padding * 2 + self.n_but_vertical * self.size_button + 25

        first_pixel_x = self.padding
        first_pixel_y = self.height_up_layout + self.padding

        self.ui.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, self.width, self.height_up_layout))
        self.resize(self.width, self.height)

        self.buttons = []
        for i in range(self.n_but_vertical):
            self.buttons.append([])
            for j in range(self.n_but_horizont):
                self.buttons[i].append(CellButton(self.centralWidget()))
                self.buttons[i][j].setGeometry(QtCore.QRect(first_pixel_x + j * self.size_button,
                                                            first_pixel_y + i * self.size_button,
                                                            self.size_button, self.size_button))
                self.buttons[i][j].setStyleSheet('''background-color: rgb(213, 213, 213)''')
                self.buttons[i][j].setFont(Qt.QFont('MS Shell Dlg 2', int(self.size_button/3)))
                self.buttons[i][j].x_button = j
                self.buttons[i][j].y_button = i
                self.buttons[i][j].clicked.connect(self.click_button)
                self.buttons[i][j].show()

        self.saper_game = Saper(self.n_but_horizont, self.n_but_vertical, self.n_mines)
        self.ui.label_mine_left.setText(str(self.n_mines))
        self.time_sec = 0
        self.ui.label_time.setText('0')

    def click_button(self):
        button = self.sender()
        if button.mine or not button.hide:
            return
        x, y = button.x_button, button.y_button
        mine_arr = self.saper_game.click(x, y)
        if mine_arr == -1:
            button.setStyleSheet('''background-color: rgb(255, 0, 0)''')
            self.game_over()
            return
        for cell in mine_arr:
            x, y = cell[0][0], cell[0][1]
            quantity = cell[1]
            self.buttons[y][x].setStyleSheet('''background-color: rgb(255, 255, 255)''')
            self.buttons[y][x].setText(str(quantity))
            self.buttons[y][x].hide = False
        quantity_not_hide = 0
        for i in range(self.n_but_vertical):
            for j in range(self.n_but_horizont):
                if self.buttons[i][j].hide:
                    quantity_not_hide += 1
        print(quantity_not_hide)
        if self.n_mines == quantity_not_hide:
            self.victory(1)

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if e.button() == QtCore.Qt.RightButton:
            quantity_blue_cells = 0
            quantity_find_mines = 0
            for i in range(self.n_but_vertical):
                for j in range(self.n_but_horizont):
                    if self.buttons[i][j].mine:
                        quantity_blue_cells += 1
                        if self.saper_game.grid[i][j].is_mine:
                            quantity_find_mines += 1
            self.ui.label_mine_left.setText(str(self.n_mines - quantity_blue_cells))
            if self.n_mines == quantity_find_mines and self.n_mines == quantity_blue_cells:
                self.victory(0)

    def victory(self, i):
        mes = Qt.QMessageBox()
        if i == 0:
            mes.setText('Поздравляю, вы нашли все мины!')
        elif i == 1:
            mes.setText('Поздравляю, вы открыли все клетки')
        mes.setWindowTitle('Победа')
        mes.setDefaultButton(Qt.QMessageBox().Ok)
        return_value = mes.exec()
        if return_value == Qt.QMessageBox().Ok:
            self.restart_game()

    def game_over(self):
        mes = Qt.QMessageBox()
        mes.setText('К сожалению вы проиграли\nПопробуйте еще раз')
        mes.setWindowTitle('Игра окончена')
        mes.setDefaultButton(Qt.QMessageBox().Ok)
        return_value = mes.exec()
        if return_value == Qt.QMessageBox().Ok:
            self.restart_game()

    def restart_game(self, n_but_horizont=None, n_but_vertical=None, n_mines=None):
        for i in range(self.n_but_vertical):
            for j in range(self.n_but_horizont):
                self.buttons[i][j].deleteLater()
        self.set_n_cells_mines(n_but_horizont, n_but_vertical, n_mines)
        self.create_window()




app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec_())
