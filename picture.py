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
    """ Devuelve el espejo vertical de la imagen """
    vertical = [value[::-1] for value in self.img]
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = self.img[::-1]
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = [''.join(self._invColor(i) for i in row) for row in self.img]
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    join = [row1 + row2 for row1, row2 in zip(self.img, p.img)]
    return Picture(join)

  def up(self, p):
    up = p.img + self.img
    return Picture(up)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    under = [
        ''.join(c1 if c2 == ' ' else c2 for c1, c2 in zip(row1, row2))
        for row1, row2 in zip(self.img, p.img)
    ]
    return Picture(under)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
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
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotate = []
    for i in range(len(self.img[0])):
      new_row = ""
      for row in reversed(self.img):
        new_row += row[i]
      rotate.append(new_row)
    return Picture(rotate)

