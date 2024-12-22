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
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = self.img[::-1]
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for row in self.img:
      new_row = ""
      for i in row:
        new_row += self._invColor(i)
      negative.append(new_row)
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    join = []
    for i in range(len(self.img)):
      join.append(self.img[i] + p.img[i]) 
    return Picture(join)

  def up(self, p):
    up = p.img.copy()
    up.extend(self.img)
    return Picture(up)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    under = []
    for i in range(len(self.img)):
      new_row = ""
      for j in range(len(self.img[i])):
        if p.img[i][j] == " ":
          new_row += self.img[i][j]
        else:
          new_row += p.img[i][j]
      under.append(new_row)
    return Picture(under)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    horizontalRepeat = []
    for value in self.img:
      horizontalRepeat.append(value*n)
    return Picture(horizontalRepeat)

  def verticalRepeat(self, n):
    verticalRepeat = []
    for i in range(n):
      verticalRepeat.extend(self.img)
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

