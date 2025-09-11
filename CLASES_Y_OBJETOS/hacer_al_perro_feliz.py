# Autor: Stive Ferney Rodriguez Silva

# En este programa se "Hace a un perro feliz" por medio de clases y objetos

class Perro:
    def __init__(self, nombre, felicidad):
        self.nombre = nombre
        self.felicidad = felicidad

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

def main():
    mi_perro = Perro("Toby",0)
    while mi_perro.felicidad < 10:
        mi_perro.comer()
        mi_perro.juguete()
        mi_perro.caricia()
    print(f"El perro {mi_perro.nombre} es feliz")

main()