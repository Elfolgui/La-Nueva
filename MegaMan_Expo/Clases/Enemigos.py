from .Base import Base

class Enemigo(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)
        Base.sprites.add(self)
        Base.Enemigos.add(self)
