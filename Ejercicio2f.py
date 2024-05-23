from interpreter import draw
from chessPictures import *

row = square.join(square.negative()).horizontalRepeat(4)
table = row.negative().up(row).verticalRepeat(2)
draw(table)