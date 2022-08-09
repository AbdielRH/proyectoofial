respuesta = "s"
contar=0
while respuesta == "s":
    diccionario = {"codigo":["1", "2", "3", "4", "5"], "nombre":["Tallarin", "Atun en trozo", "leche", "Filete", "fideos largos"], "precio":["5", "4", "5", "7", "2"]}
    print(diccionario)
    for key in diccionario:
        print(key, ":", diccionario[key])
    codigo = input("Ingresa el código: ")
    cantidad = int(input("Ingresa la cantidad: "))
    if codigo == "e-001":
        precio = 5
        nomproduc = "azúcar"
    elif codigo == "e-002":
        precio = 4
        nomproduc = "arroz"
    elif codigo =="e-003":
        precio = 5
        nomproduc = "leche"
    elif codigo == "e-004":
        precio = 7
        nomproduc = "atún"
    elif codigo == "e-005":
        precio = 2
        nomproduc = "fideos largos"
    print("El codigo es: ",codigo)
    print("El nombre del producto es :", nomproduc)
    print("La cantidad es: ",cantidad)
    print("El precio es: ",precio)
    total = precio * cantidad
    print("El monto es: ", total)
    print("Desea continuar Si (s) o No (n)")
    respuesta = input()
    contar += total
    tupla = [str(codigo), " ", nomproduc, " ", str(cantidad), " ", str(precio), " ", str(total)]
    cadenavalores = "".join(tupla)
    f = open("demofile.txt", "a")
    f.write("\n" + cadenavalores)
    f.close()
f = open("demofile.txt")
print(f.read())
f.close()
print("El precio a pagar es: ",contar)