import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor, QFont, QIntValidator
from PyQt6.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication, QGridLayout, QFrame)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.grid = None
        self.initUI()


    def resizeEvent(self, event):
        # Get the current window size
        self.adjustWindowSize()
        self.adjustFontSizes()
        self.adjustGridLayoutSpacing()


        event.accept()

    def initUI(self):

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setSpacing(5)
        self.setProperty("class", "window")  # Set background color


        # tiles = [[_ for _ in range(1, 10)] for _ in range(1, 10)]

        for row in range(9):
            for col in range(9):
                # tile = tiles[row][col]
                # if tile == '':
                #     continue
                tile_label = QLineEdit()
                tile_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

                validator = QIntValidator(1, 9)
                tile_label.setValidator(validator)

                self.grid.addWidget(tile_label, row, col)

                if row // 3 % 2 == col // 3 % 2:
                    tile_label.setProperty("class", "box1")
                else:
                    tile_label.setProperty("class", "box2")

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Sudoku Solver')

    # def onChanged(self, text):
    #
    #     self.lbl.setText(text)
    #     self.lbl.adjustSize()


    def adjustWindowSize(self):
        current_size = self.size()
        # Adjust the width and height to maintain the aspect ratio
        aspect_ratio = 1  # Set your desired aspect ratio here
        if current_size.width() != current_size.height() * aspect_ratio:
            new_width = current_size.height() * aspect_ratio
            self.resize(new_width, current_size.height())

    def adjustFontSizes(self):
        windowWidth = self.width()

        # Calculate the font size based on the window width
        fontSize = int(windowWidth / 25)  # Adjust the division factor to your preference

        # Create a QFont object with the desired font family and size
        font = QFont("Beirut", fontSize)

        # Iterate through all QLineEdit widgets and set the font
        for child in self.findChildren(QLineEdit):
            child.setFont(font)


    def adjustGridLayoutSpacing(self):
        windowWidth = self.width()

        # Calculate the spacing based on the window width
        spacing = int(windowWidth / 100)  # Adjust the division factor to your preference

        # Set the spacing for the QGridLayout
        self.grid.setSpacing(spacing)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    with open("styles.css", "r") as file:
        app.setStyleSheet(file.read())

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
