import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import QWidget, QLineEdit, QApplication, QGridLayout, QVBoxLayout, QLabel, QHBoxLayout, \
    QPushButton, QSizePolicy, QMessageBox
import sudoku_algorithms


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.grid_layout = None
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)
        self.setWindowTitle('Sudoku Solver')

        # Labels
        word_layout = QHBoxLayout()
        title_label = QLabel("Sudoku Solver", alignment=Qt.AlignmentFlag.AlignLeft)
        title_label.setProperty("class", "title")
        info_label = QLabel("Add current sudoku numbers to grid and hit calculate to solve the board.", alignment=Qt.AlignmentFlag.AlignCenter)
        info_label.setProperty("class", "info")
        word_layout.addWidget(title_label)
        word_layout.addWidget(info_label)
        main_layout.addLayout(word_layout)

        # Grid
        self.grid_layout = QGridLayout()
        main_layout.addLayout(self.grid_layout)
        self.setProperty("class", "window")  # Set background color
        self.grid_layout.setSpacing(0)  # Set the spacing between items in the grid to 0
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        for row in range(9):
            for col in range(9):
                tile_label = QLineEdit(alignment=Qt.AlignmentFlag.AlignCenter)
                tile_label.setValidator(QIntValidator(1, 9))
                tile_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                self.grid_layout.addWidget(tile_label, row, col)

                box_class = "box1" if (row // 3 % 2 == col // 3 % 2) else "box2"
                if (row + col) % 2 != 0:
                    box_class += "-odd"
                tile_label.setProperty("class", box_class)

        # Buttons
        solve_button = QPushButton("Solve")
        solve_button.clicked.connect(self.onSolve)  # Connect the button's clicked signal to the onSolve slot
        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.onReset)  # Connect the button's clicked signal to the onReset slot
        button_layout = QHBoxLayout()
        button_layout.addWidget(solve_button)
        button_layout.addWidget(reset_button)
        main_layout.addLayout(button_layout)

        self.adjustFontSizes()

    def resizeEvent(self, event):
        current_size = self.size()
        new_size = QSize(current_size.width(), current_size.height())  # Get the current size of the window

        # Constrain the resizing to a diagonal aspect ratio
        if new_size.width() != new_size.height():
            if new_size.width() > new_size.height():
                new_size.setWidth(new_size.height())
            else:
                new_size.setHeight(new_size.width())

        self.resize(new_size)  # Set the new size of the window


    def adjustFontSizes(self):
        window_width = self.width()
        font_size = int(window_width / 15)
        font = QFont("Beirut", font_size)

        for child in self.findChildren(QLineEdit):
            child.setFont(font)

    def onSolve(self):
        box_contents = []
        for row in range(9):
            row_contents = []
            for col in range(9):
                widget = self.grid_layout.itemAtPosition(row, col).widget()
                text = widget.text()
                if text == "":
                    text = "."
                row_contents.append(text)
            box_contents.append(row_contents)

        print(box_contents)
        if sudoku_algorithms.isValidSudoku(self, box_contents):
            print("Valid Sudoku board")
            sudoku_algorithms.solveSudoku(self, box_contents)
            print(box_contents)
            self.setSolution(box_contents)
        else:
            QMessageBox.critical(self, "Invalid Sudoku Board", "Not a valid Sudoku board.")

    def onReset(self):
        for row in range(9):
            for col in range(9):
                widget = self.grid_layout.itemAtPosition(row, col).widget()
                widget.setText("")

    def setSolution(self, box_contents):
        for row in range(9):
            for col in range(9):
                widget = self.grid_layout.itemAtPosition(row, col).widget()
                widget.setText(box_contents[row][col])

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    with open("styles.css", "r") as file:
        app.setStyleSheet(file.read())

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
