# Autor
# Descripcion

def hola():
    print("Hola Mundo ")

def operation():
        for i in (10,"casa",-3):
              if(i=="casa"):
                print(f"La palabra {i} ")


     

# Funciones
# Diseñar una encuesta para 6 users,
# Nombre 
# Carrera
# Idea de proyecto

list_nombre = [1,2,3,4,5,6]
list_carrera = [1,2,3,4,5,6]
list_idea = [1,2,3,4,5,6]

def encuesta():
  for i in range(2,7):
    list_nombre[i] = input("¿Como se llama? ")
    list_carrera[i] = input("Que carrera estudia? ")
    list_idea[i] = input("¿Ya tienes una idea de proyecto?¿Cuál?")



