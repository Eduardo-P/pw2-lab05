from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    vertical = [value[::-1] for value in self.img]
    return Picture(vertical)

  def horizontalMirror(self):
    horizontal = self.img[::-1]
    return Picture(horizontal)

  def negative(self):
    negative = [
      ''.join(self._invColor(i) for i in row)
      for row in self.img
    ]
    return Picture(negative)

  def join(self, p):
    join = [row1 + row2 for row1, row2 in zip(self.img, p.img)]
    return Picture(join)

  def up(self, p):
    up = p.img + self.img
    return Picture(up)

  def under(self, p):
    under = [
      ''.join(c1 if c2 == ' ' else c2 for c1, c2 in zip(row1, row2))
      for row1, row2 in zip(self.img, p.img)
    ]
    return Picture(under)
  
  def horizontalRepeat(self, n):
    horizontalRepeat = [
      ''.join(value for i in range(n)) 
      for value in self.img
    ]
    return Picture(horizontalRepeat)

  def verticalRepeat(self, n):
    verticalRepeat = [
      row for i in range(n)
      for row in self.img
    ]
    return Picture(verticalRepeat)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    rotate = [
      ''.join(self.img[j][i] for j in range(len(self.img) - 1, -1, -1))
      for i in range(len(self.img[0]))
    ]
    return Picture(rotate)