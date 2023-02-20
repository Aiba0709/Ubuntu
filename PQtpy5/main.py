from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 

def add_button_lable():
    print("Hello world")

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Простая программа")
    window.setGeometry(300, 250, 500, 500)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Hello World ")
    main_text.move(100,0)

    button = QtWidgets.QPushButton(window)
    button.setText("Нажми на меня")
    button.clicked.connect(add_button_lable)

    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    application()

         