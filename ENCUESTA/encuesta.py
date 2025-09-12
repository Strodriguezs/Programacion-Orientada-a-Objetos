# Autor: Stive Ferney Rodríguez Silva

# Hacer una encuesta para 10 USUARIOS 
#peguntas: Usted sabe trabajar en equipo?, cual es su nivel en pithon?, cual es su idea de proyecto

class Encuesta:
    def __init__(self):
        # Atributos principales
        self.preguntas = ["¿Cómo se llama?",
                          "¿Qué edad tiene?",
                          "¿Qué tema prefieres para el proyecto?"]
        self.respuestas = []  # lista de diccionarios, uno por cada estudiante

    def agregar_respuesta(self):
        respuesta_estudiante = {}

        # Se recorren las preguntas y se guarda la respuesta en un diccionario
        for pregunta in self.preguntas:
            respuesta = input(pregunta)
            respuesta_estudiante[pregunta] = respuesta
        # Se agrega al listado general
        self.respuestas.append(respuesta_estudiante)

    def mostrar_resultados(self):
      for i in range(1, 11):  # siempre 10 estudiantes
          resp = self.respuestas[i-1]  # accedemos al diccionario en la posición i-1
          print(f"\nEstudiante {i}:")
          for pregunta, respuesta in resp.items():
              print(f"  {pregunta}: {respuesta}")


# Programa principal
def main():
  encuesta = Encuesta()

  for _ in range(10):  # asegura mínimo 10 respuestas
    encuesta.agregar_respuesta()

  # Mostrar resultados al final
  encuesta.mostrar_resultados()

main()


# Al final se debe stablecer un grupo maximo de 3 estudiantes y por lo menos 2 ideas de proyecto.
