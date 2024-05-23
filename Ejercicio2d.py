from interpreter import draw
from chessPictures import *

table = square.join(square.negative()).horizontalRepeat(4)
draw(table)