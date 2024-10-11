# Clase: es una plantilla que define características y comportamientos de un objeto
class Robot:
    # Constructor: es un método especial que se ejecuta al crear una instancia y permite inicializar los atributos
    # Self se refiere a la instancia específica
    def __init__(self, nombre, tipo):
        # Atributos o características
        self.nombre = nombre
        self.tipo = tipo

    # Método: es una función que define el comportamiento o acción de un objeto
    def saludar(self):
        print(f"¡Hola! Soy {self.nombre} y soy un robot en una muestra de Robots y hablo gracias a una IA")

    def hacer_truco(self):
        if self.tipo == "Humanoide":
            print(f"Soy {self.nombre} y estoy haciendo el paso del Robot")
        else:
            print(f"Soy {self.nombre} de tipo {self.tipo} por favor denme instrucciones")

# Instancia: que es un objeto específico creado a partir de la plantilla llamada clase
robotin = Robot("Robotín", "Humanoide")
tostadora = Robot("Tosty", "Electrodoméstico")

# robotin.saludar()
# tostadora.saludar()

# robotin.hacer_truco()
tostadora.hacer_truco()