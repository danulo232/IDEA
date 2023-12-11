import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.centrwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centrwidget)
        self.setWindowTitle("Нотатки")
        self.resize(1100, 680)
        #вікно по центру дисплея
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.menu()
        self.widgets_1()
    #створення меню
    def menu(self):
        #work file
        new_file = QAction('Новий', self)
        new_file.setShortcut('Ctrl+O')
        new_file.triggered.connect(self.create_new_file)

        open_file = QAction('Відкрити', self)
        open_file.setShortcut('Ctrl+E')
        open_file.triggered.connect(self.open_file)

        save_file = QAction('Зберегти', self)
        save_file.setShortcut('Ctrl+S')
        save_file.triggered.connect(self.save_file)

        pass_1 = QAction('', self)

        menu_exit = QAction('Вихід', self)
        menu_exit.setShortcut('Ctrl+Q')
        menu_exit.triggered.connect(qApp.quit)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(new_file)
        file_menu.addAction(open_file)
        file_menu.addAction(save_file)
        file_menu.addAction(pass_1)
        file_menu.addAction(menu_exit)

        #tema
        tema_black = QAction('Темна', self)
        tema_black.triggered.connect(self.tems_black)

        tema_white = QAction('Світла', self)
        tema_white.triggered.connect(self.tems_one)

        system_tems = menu_bar.addMenu('Тема')
        system_tems.addAction(tema_black)
        system_tems.addAction(tema_white)


    #створення нового файлу
    def create_new_file(self):
        try:
            open_qwe = QFileDialog.getOpenFileName(self)[0]
            f = open(open_qwe, 'r', encoding='utf-8')
            with f:
                text_code = f.read()
                self.code_input.setText(text_code)
        except FileNotFoundError:
            pass
    #відкривання файлу
    def open_file(self):
        try:
            open_qwe = QFileDialog.getOpenFileName(self)[0]
            f = open(open_qwe, 'r', encoding='utf-8')
            with f:
                text_code = f.read()
                self.code_input.setText(text_code)
        except FileNotFoundError:
            pass
        self.statusBar().showMessage('Вікриття файлу')
    #збереження файлів
    def save_file(self):
        try:
            open_qwe = QFileDialog.getSaveFileName(self)[0]
            f = open(open_qwe, 'w', encoding='utf-8')
            text_save = self.code_input.toPlainText()
            f.write(text_save)
            f.close()
        except FileNotFoundError:
            pass
        self.statusBar().showMessage('Збереження файлу')

    #створення віджетів
    def widgets_1(self):
        # вкладки
        #self.tabwidget = QTabWidget()

        self.code_input = QtWidgets.QTextEdit(self)
        self.code_input.setFont(QFont("Arial", 12))
        self.text_code_input = QtWidgets.QLabel(self)
        self.text_code_input.setFont(QFont("Arial", 9))
        self.text_code_input.setText('Код:')

        #slider
        self.slider_mashtab = QSlider(Qt.Horizontal)
        self.slider_mashtab.setFixedWidth(150)
        self.slider_mashtab.setMinimum(0)
        self.slider_mashtab.setMaximum(10)
        self.slider_mashtab.valueChanged.connect(self.setting_slider_mashtab)
        self.label_scale = QLabel(self)
        self.label_scale.setFixedWidth(20)
        self.label_scale.setFont(QFont("Arial", 10))

        #name = None
        #self.tabwidget.addTab(self.code_input, name)
        
        self.geometry_ = QtWidgets.QGridLayout(self.centrwidget)
        self.geometry_.addWidget(self.text_code_input, 1, 1)
        self.geometry_.addWidget(self.code_input, 2, 1, 1, 3)
        #self.geometry_.addWidget(self.tabwidget, 2, 1, 1, 3)
        self.geometry_.addWidget(self.slider_mashtab, 1, 3)
        self.geometry_.addWidget(self.label_scale, 1, 4)


    #slider settings
    def setting_slider_mashtab(self):
        self.size_ = self.slider_mashtab.value()
        self.label_scale.setText(str(self.size_))

        if self.size_ == 1:
            self.code_input.setFont(QFont("Arial", 8))
        if self.size_ == 2:
            self.code_input.setFont(QFont("Arial", 9))
        if self.size_ == 3:
            self.code_input.setFont(QFont("Arial", 10))
        if self.size_ == 4:
            self.code_input.setFont(QFont("Arial", 12))
        if self.size_ == 5:
            self.code_input.setFont(QFont("Arial", 14))
        if self.size_ == 6:
            self.code_input.setFont(QFont("Arial", 16))
        if self.size_ == 7:
            self.code_input.setFont(QFont("Arial", 18))
        if self.size_ == 8:
            self.code_input.setFont(QFont("Arial", 20))
        if self.size_ == 9:
            self.code_input.setFont(QFont("Arial", 21))
        if self.size_ == 10:
            self.code_input.setFont(QFont("Arial", 22))
        

    #tems
    def tems_black(self):
        self.code_input.setStyleSheet("background-color: rgb(70, 70, 70);color: rgb(11, 255, 247)")
        self.text_code_input.setStyleSheet("background-color: rgb(70, 70, 70);color: rgb(11, 255, 247)")
        self.centrwidget.setStyleSheet("background-color: rgb(70, 70, 70);color: rgb(11, 255, 247)")

    '''def tems_white(self):
        self.code_input.setStyleSheet("background-color: rgb(85, 85, 255);color: rgb(255, 244, 244);")
        self.text_code_input.setStyleSheet("background-color: rgb(85, 85, 255);color: rgb(255, 244, 244);")
        self.centrwidget.setStyleSheet("background-color: rgb(85, 85, 255);color: rgb(255, 244, 244);")
      '''  
    def tems_one(self):
        self.code_input.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);")
        self.text_code_input.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);")
        self.centrwidget.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0, 0, 0)")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())