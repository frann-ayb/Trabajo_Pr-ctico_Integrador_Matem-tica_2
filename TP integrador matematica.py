registro = []
estado = True
while estado:
    dni = input("propocione su numero de dni, para continuar ingrese alguna letra: ")
    dni = dni.replace(".", "").replace(",", "")
    try:
        dni = int(dni)
    except:
        print("\nDNI/s registrados...")

    if type(dni) is int:
        registro.append(dni)
    else:
        estado = False
print(registro)
conjuntos = []


for i in range(0, len(registro)):
    conjunto = []
    for c in str(registro[i]): 
        conjunto.append(c)
    conjuntos.append(conjunto)

print(conjuntos)

