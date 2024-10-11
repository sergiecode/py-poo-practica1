# Clase Padre (superclase)
class Personaje:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
    
    def presentarse(self):
        print(f"¡Hola! Soy {self.nombre} y mi poder es {self.poder}")

# Clase derivada (subclase)
class Superheroe(Personaje):
    def __init__(self, nombre, poder, ciudad):
        super().__init__(nombre, poder) # Utilizaremos super para pasarle la información a la superclase
        self.ciudad = ciudad

    def salvar_la_ciudad(self):
        print(f"{self.nombre} está salvando {self.ciudad} usando su poder {self.poder}")

# Clase derivada (subclase)
class Villano(Personaje):
    def __init__(self, nombre, poder, arhienemigo):
        super().__init__(nombre, poder)
        self.archienemigo = arhienemigo

    def plan_maligno(self):
        print(f"¡Cuidado! {self.nombre} está organizando un plan malvado en contra de {self.archienemigo} usando su gran poder {self.poder}")


heroe = Superheroe("Captain Código", "supermegarefactorización", "Python City")
villano = Villano("Bugman", "Crear errores en tus aplicaciones favoritas", "Captain Codigo")

heroe.presentarse()
villano.presentarse()

heroe.salvar_la_ciudad()
villano.plan_maligno()

