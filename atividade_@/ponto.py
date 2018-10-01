class Ponto():
    """
        Classe Ponto, usando como exemplo um plano cartesiano
    """
    # atributos
    x = None
    y = None

    # comportamentos ou metódos
    def mover(self, x, y):
        self.x, self.y = x, y


    def quadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primeiro quadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo quadrante"
        elif self.x < 0 and self.y < 0:
            return "Terceiro quadrante"
        elif self.x > 0 and self.y < 0:
            return "Quarto quadrante"
        elif self.x == 0 and self.y == 0:
            return "Origem"

# uso da classe
ponto1 = Ponto()
ponto1.x = 0
ponto1.y = 0
ponto1.mover(-0, -1)
resultado = ponto1.quadrante()
print(resultado)
    
