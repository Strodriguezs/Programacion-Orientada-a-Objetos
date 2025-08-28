# Autor: Stive Ferney Rodriguez Silva

# Esto es una prueba para novatos 

# Ejecute una entrada de texto e imprímala 

a = input("Ingrese su nombre completo  ")

print(f"Su nombre completo es {a}")

# Realizar las tablas de multiplicar del número que usted ingrese

b=int(input("Ingrese el numero del cual quiere conocer sus tablas de multiplicar "))

i=1
while(i<=10):
	print(f"{b} x {i} = {b*i}")
	i=i+1
# Utilizando una función obtenga el numero factorial de un número dado

c=int(input("ingrese el numero del cual quiere conocer su factorial "))
j=c-1

def factorial(c,j):
	if(c<0): 
		print("Error")
	elif(c==0):
		print(1)
	elif(c==1):
		print(0)
	else:
		while(c>0 and j>0):
			c=c*j
			j=j-1
		print(f"el numero factorial es {c}")

factorial(c,j)