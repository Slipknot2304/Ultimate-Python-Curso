"""Ejercicios en Python Sesion 1"""

# Ejecicio uno
nombre_usuario = input("Cual es tu nombre?")
cuantos_hay = int(input("Cuantos reps crees que tengan el mismo nombre?"))
reps = f"{nombre_usuario} {"\n"}"
print(reps * cuantos_hay)

# Ejercicio dos
print(nombre_usuario.upper())
print(nombre_usuario.lower())
print(f"{nombre_usuario.title()} {"\n"}")

# Ejercicio tres
n = len(nombre_usuario)
print(f"{nombre_usuario.upper()} {n}")

# Ejercicio cuatro
telefono = input("Escribe tu telefono con prefijo y extencion (14 numeros):")

print("Tu telefono sin prefijo ni extencion es este?:")
print(telefono[2:12])
