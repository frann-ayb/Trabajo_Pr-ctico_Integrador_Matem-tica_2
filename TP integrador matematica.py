from datetime import datetime
from itertools import product

registros = []
dni_nums = []
#solicitamos al usuario ingresar la cantidad de DNIs con los que quiere trabajar
cantidad_dnis = 0
while cantidad_dnis < 2: #establece la cantidad minima en 2
    cantidad_dnis = int(input("Ingresa la cantidad de DNIs que quiere ingresar(minimo 2): "))
#Mediante la función set(), se crean los conjuntos de dígitos únicos, y se almacenan todos los conjuntos creados en una lista llamada registro
for i in range(1,cantidad_dnis+1):
    dni = input("Propocione su numero de dni: ")
    dni = dni.replace(",", "").replace(".", "") #elimina caracteres no numericos.
    mi_set = set(dni)
    dni_nums.append(dni)
    registros.append(mi_set)

print("\n DNI/s registrados...")
print(dni_nums)
print("---------------------------")

contador_de_numeros=[]

for n in range(cantidad_dnis): #muestra las veces que se repite cada digito
    contador_de_numeros.clear() 
    for l in range(10): 
        contador = 0
        for i in dni_nums[n]:
                if str(l) == i:
                    contador += 1
        if contador != 0:
            contador_de_numeros.append(f"{l} : {contador} veces")
    print(f"Frecuencia de números en el DNI {dni_nums[n]}:")
    print(contador_de_numeros)

#uso de los métodos de la función set() para realizar las operaciones de union, intersección, diferencia y diferencia simétrica
union = set().union(*registros)
interseccion = set.intersection(*registros)
diferencia = set.difference(*registros)
if cantidad_dnis == 2:
    diferencia_simetrica = set.symmetric_difference(*registros)
else:
    diferencia_simetrica = union - interseccion     #evita el error de la funcion symmetric_difference

print("---------------------------")
print(f"La unión de los conjuntos es: {union}")
if interseccion == set():      #mejora la resolucion ante conjuntos vacios
    print("La intersección de los conjuntos es:{}")
else:
    print(f"La intersección de los conjuntos es: {interseccion}")
if diferencia == set():
    print("La diferencia de los conjuntos es:{}")
else:
    print(f"La diferencia de los conjuntos es: {diferencia}")
if diferencia_simetrica == set():
    print("La diferencia simétrica de los conjuntos es: {}")
else:
    print(f"La diferencia simétrica de los conjuntos es: {diferencia_simetrica}")
print("---------------------------")




#Suma de los dígitos del conjunto
for registro in registros:
    registro_int={int(x) for x in registro}
    suma_digitos = sum(registro_int)
    print(f"La suma de los dígitos del conjunto es: {suma_digitos}")
print("---------------------------")

#Evaluación de expresiones lógicas
for i in registros:
    if len(i)>=6:
        print(f"La Diversidad Numérica del conjunto {i} es Alta")
if len(interseccion)>0:
    print(f"Los dígitos compartidos son: {interseccion}")

# B. Operaciones con años de nacimiento



# Función para determinar si un año es bisiesto
def bisiesto(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Ingreso de los años de nacimientos.
birth_year = []
cantidad = int(input("¿Cuántos integrantes hay en el grupo? "))

for i in range(cantidad): # Ciclo repetitivo de acuerdo a la cantidad ingresada arriba
    year = int(input(f"Ingresá el año de nacimiento de la persona {i+1}: "))
    while year in birth_year: # Validar que el año ya fue ingresado
        print("Ese año ya fue ingresado. Por favor ingresa otro año.")
        year = int(input(f"Ingresá nuevamente el año de nacimiento de la persona {i+1}: "))
    birth_year.append(year)

# Calcular cuantos nacieron en años pares e impares
par = 0
impar = 0

for year in birth_year:
    if year % 2 == 0:
        par += 1
else:
    impar += 1

print(f"\nCantidad de personas nacidas en años pares: {par}")
print(f"Cantidad de personas nacidas en años impares: {impar}")

# Si todos nacieron después del 2000
if all(year > 2000 for year in birth_year):
    print("Grupo Z")

# Si alguno nació en año bisiesto
if any (bisiesto(year) for year in birth_year):
    print("Tenemos un año especial")

# Calcular edades
actual_year = datetime.now().year
edades = [actual_year - year for year in birth_year]

# Producto cartesiano entre conjunto de años y conjunto de edades
producto_cartesiano = list(product(birth_year, edades))

print("\nProducto cartesiano entre años de nacimiento y edades actuales:")
for par in producto_cartesiano:
    print(f"Año: {par[0]}, Edad: {par[1]}")
