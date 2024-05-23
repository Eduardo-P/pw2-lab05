from interpreter import draw
from chessPictures import *

table = queen.horizontalRepeat(4)
table = table.rotate()

draw(table)