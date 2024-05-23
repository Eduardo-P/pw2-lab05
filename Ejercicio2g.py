from interpreter import draw
from chessPictures import *

row = square.join(square.negative()).horizontalRepeat(4)

rowPawns = row.under(pawn.horizontalRepeat(8))

rowPieces = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
rowPieces = row.negative().under(rowPieces)

table = rowPieces.up(rowPawns)
table = table.up(row.negative().up(row).verticalRepeat(2))
table = table.up(rowPawns.up(rowPieces).negative())

draw(table)