registros = []
#solicitamos al usuario ingresar la cantidad de DNIs con los que quiere trabajar
cantidad_dnis = int(input("Ingresa la cantidad de DNIs que quiere ingresar: "))
#Mediante la función set(), se crean los conjuntos de dígitos únicos, y se almacenan todos los conjuntos creados en una lista llamada registro
for i in range(1,cantidad_dnis+1):
    dni = input("Propocione su numero de dni: ")
    mi_set = set(dni)
    registros.append(mi_set)
print(registros)
print("---------------------------")

#uso de los métodos de la función set() para realizar las operaciones de union, intersección, diferencia y diferencia simétrica
union = set().union(*registros)
interseccion = set.intersection(*registros)
diferencia = set.difference(*registros)
diferencia_simetrica = set.symmetric_difference(*registros)
print("---------------------------")

print(f"La unión de los conjuntos es: {union}")
print(f"La intersección de los conjuntos es: {interseccion}")
print(f"La diferencia de los conjuntos es: {diferencia}")
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
