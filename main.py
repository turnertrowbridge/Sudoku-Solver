import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import (QWidget, QLineEdit, QApplication, QGridLayout, QSizePolicy)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        # self.setFixedSize(600, 600)
        self.line_edit_size = None
        self.grid = None
        self.initUI()

    def resizeEvent(self, event):
        # Get the current window size
        self.adjustWindowSize()
        self.adjustFontSizes()
        # self.adjustLineEditSizes()
        event.accept()

    def initUI(self):

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setProperty("class", "window")  # Set background color
        self.grid.setSpacing(0)  # Set the spacing between items in the grid to 0
        self.grid.setContentsMargins(0, 0, 0, 0)

        self.line_edit_size = 50

        # tiles = [[_ for _ in range(1, 10)] for _ in range(1, 10)]

        for row in range(9):
            for col in range(9):
                # tile = tiles[row][col]
                # if tile == '':
                #     continue
                tile_label = QLineEdit()
                tile_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                tile_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                validator = QIntValidator(1, 9)
                tile_label.setValidator(validator)
                # tile_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

                self.grid.addWidget(tile_label, row, col)

                if row // 3 % 2 == col // 3 % 2:
                    if (row + col) % 2 == 0:
                        tile_label.setProperty("class", "box1")
                    else:
                        tile_label.setProperty("class", "box1-odd")
                else:
                    if (row + col) % 2 == 0:
                        tile_label.setProperty("class", "box2")
                    else:
                        tile_label.setProperty("class", "box2-odd")

        self.setGeometry(100, 100, 100, 100)
        self.setWindowTitle('Sudoku Solver')

        self.adjustFontSizes()  # Call the method initially to set the font sizes

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
        fontSize = int(windowWidth / 15)  # Adjust the division factor to your preference

        # Create a QFont object with the desired font family and size
        font = QFont("Beirut", fontSize)

        # Iterate through all QLineEdit widgets and set the font
        for child in self.findChildren(QLineEdit):
            child.setFont(font)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    with open("styles.css", "r") as file:
        app.setStyleSheet(file.read())

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
