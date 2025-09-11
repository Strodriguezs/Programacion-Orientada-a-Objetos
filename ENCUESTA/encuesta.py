# Autor: Stive Ferney Rodríguez Silva

# Hacer una encuesta para 10 USUARIOS 
#peguntas: Usted sabe trabajar en equipo?, cual es su nivel en pithon?, cual es su idea de proyecto

class encuesta:
    def __init__(self, preguntas, respuestas):
        self.preguntas = preguntas
        self.respuestas = respuestas
    def agregar_respuesta(self):
        self.respuestas=[0,1,2,3,4,5,6,7,8,9]
        for i in range (0,10):
            self.preguntas = [input("¿Cual es su nombre?"),input("¿Que edad tiene?"),input("Si tiene una idea de proyecto diga cual es")]
            self.respuestas[i] = self.preguntas
        return self.respuestas
    def mostrar_resultados(self):
        print(self.respuestas)


# Al final se debe stablecer un grupo maximo de 3 estudiantes y por lo menos 2 ideas de proyecto.
