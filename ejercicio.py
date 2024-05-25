numero=int(input("Intrudoce un número entero positivo: "))
if numero<0:
    print("Error: introduce un numeero valido ")
else:
    cuenta_atras =[]
    for i in range(numero, -1,-1):
        cuenta_atras.append(str(i))
    resultad=".".join(cuenta_atras)
    print("Los numeros en orden decendiente es: ", resultad)