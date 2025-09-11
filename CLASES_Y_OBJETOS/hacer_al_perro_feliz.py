# Autor: Stive Ferney Rodriguez Silva

# En este programa se "Hace a un perro feliz" por medio de clases y objetos

class perro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 0

    def comer(self):
        self.felicidad += 4
        print(f"El perro {self.nombre} comió, es más feliz")

    def juguete(self):
        self.felicidad += 3
        print(f"El perro {self.nombre} recibió un juguete, es más feliz")

    def caricia(self):
        self.felicidad += 3
        print(f"El perro {self.nombre} fué acariciado, es más feliz")
        


# Programa principal
dog = perro("Firulais")

def main():
    perro.comer()
    perro.juguete()
    perro.caricia()