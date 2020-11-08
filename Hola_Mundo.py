class Coche():

    def __init__(self, vin):
        self.__vin = vin
        self.__largoChasis = 220
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
        self.__gasolina = "ok"
        self.__aceite = "ok"
        self.__puertas = "cerradas"

    def arrancar(self):

        if self.__enmarcha:
            return "El coche " + self.__vin + " ya estaba arrancado"
        else:
            if self.__chequeo():
                self.__enmarcha = True
                return "Arrancando coche " + self.__vin + "......hecho"
            else:
                return "Revisa la gasolina, el aceite y que las puertas estén cerradas.\nNo podemos arrancar"

    def apagar(self):
        if self.__enmarcha:
            self.__enmarcha = False
            return "Apagando coche " + self.__vin + "......hecho"
        else:
            return "El coche " + self.__vin + " ya estaba apagado"

    def estado(self):
        print("Datos sobre coche con VIN: ", self.__vin + "\n- Largo del chasis: ", self.__largoChasis,
              "\n- Ancho chasis: ", self.__anchoChasis, "\n- Nº de ruedas: ", str(self.__ruedas))

    def __chequeo(self):
        print("Realizando chequeo interno")

        if self.__gasolina == "ok" and self.__aceite == "ok" and self.__puertas == "cerradas":
            print("Gasolina:", self.__gasolina ,"\nAceite: ", self.__aceite, "\nPuertas: ", self.__aceite)
            return True
        else:
            print("Gasolina:", self.__gasolina ,"\nAceite: ", self.__aceite, "\nPuertas: ", self.__aceite)
            return False


miCoche1 = Coche("00001")
miCoche2 = Coche("00002")

print("Intentamos arrancar miCoche1")
print(miCoche1.arrancar())
print("Intentamos apagar miCoche2")
print(miCoche2.apagar())
print("Intentamos arrancar otra vez el Coche1")
print(miCoche1.arrancar())
print("Intentamos arrancar el Coche2")
print(miCoche2.arrancar())
print("Intentamos apagar el Coche1")
print(miCoche1.apagar())

miCoche1.estado()
miCoche2.estado()
