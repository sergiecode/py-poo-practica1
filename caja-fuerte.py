class CajaFuerte:
    def __init__(self, clave, cantidad):
        self.__clave = clave
        self.__cantidad = cantidad
    
    # Getters: son métodos para poder obtener información de un atributo privado
    # def obtener_clave(self):
    #     return self.__clave

    def verificar_clave(self, clave):
        return self.__clave == clave # Devolverá TRUE si la clave que nos pasan coincide con la original

    def obtener_cantidad(self, clave):
        if self.verificar_clave(clave):
            return self.__cantidad
        else:
            print("La clave que has colocado no es correcta")
    
    # Setters: son métodos para establecer nuevos valores a los atributos privados
    def establecer_clave(self, clave_nueva, clave):
        if self.verificar_clave(clave):
            if len(clave_nueva) < 4:
                print("La clave debe tener al menos 4 caracteres")
            else:
                print("La clave fue cambiada con éxito")
                self.__clave = clave_nueva
        else:
            print("La clave que has colocado no es correcta")

    def establecer_cantidad(self, cantidad_nueva, clave):
        if self.verificar_clave(clave):
            if cantidad_nueva <= 0:
                print("No se puede colocar una cantidad negativa")
            else:
                print("La cantidad fue cambiada con éxito")
                self.__cantidad = cantidad_nueva
        else:
            print("La clave que has colocado no es correcta")

caja = CajaFuerte("1234", 1000)

caja.establecer_clave("4567", "1234")
caja.establecer_cantidad(2000, "4567")
print(caja.obtener_cantidad("4567"))