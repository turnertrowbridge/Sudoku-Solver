import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication, QGridLayout, QFrame)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(5)

        tiles = [[_ for _ in range(1, 10)] for _ in range(1, 10)]

        for row in range(len(tiles)):
            for col in range(len(tiles[row])):
                tile = tiles[row][col]
                if tile == '':
                    continue
                tile_label = QLineEdit(str(tile))
                tile_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                grid.addWidget(tile_label, row, col)

                if col % 3 == 2 and col != len(tiles[row]) - 1:
                    line = QFrame()
                    line.setFrameShape(QFrame.Shape.VLine)
                    grid.addWidget(line, row, col + 1)
                    grid.setRowStretch(row, 1)

            if row % 3 == 2 and row != len(tiles) - 1:
                for col in range(len(tiles[row])):
                    line = QFrame()
                    line.setFrameShape(QFrame.Shape.HLine)
                    grid.addWidget(line, row + 1, col)
                    grid.setColumnStretch(col, 1)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Sudoku Solver')
        self.show()

    # def onChanged(self, text):
    #
    #     self.lbl.setText(text)
    #     self.lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
