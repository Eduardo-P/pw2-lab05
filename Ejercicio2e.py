from interpreter import draw
from chessPictures import *

table = square.negative().join(square).horizontalRepeat(4)
draw(table)