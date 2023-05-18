import sys
import numpy as np
from PyQt6.QtWidgets import (QWidget, QLabel,
        QLineEdit, QApplication, QGridLayout)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        tiles = [[_ for _ in range(1, 10)] for _ in range(1, 10)]

        for row in range(len(tiles)):
            for col in range(len(tiles[row])):
                tile = tiles[row][col]
                if tile == '':
                    continue
                tile_label = QLineEdit(str(tile))
                grid.addWidget(tile_label, row, col)

        self.setGeometry(300, 300, 350, 250)
        # self.move(300, 300)
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