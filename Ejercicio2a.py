from interpreter import draw
from chessPictures import *

horseWhite = knight
horseBlack = horseWhite.negative()
row = horseBlack.join(horseWhite)
table = row.up(row.negative())
draw(table)