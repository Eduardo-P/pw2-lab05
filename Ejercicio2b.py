from interpreter import draw
from chessPictures import *

horseWhite = knight
horseBlack = horseWhite.negative().verticalMirror()
row = horseBlack.up(horseWhite)
table = row.join(row.negative())
draw(table)