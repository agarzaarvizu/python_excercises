manejador = open("../files/mbox-short.txt")
contador = 0

for linea in manejador:
    palabras = linea.split()
    if len(palabras) == 0 : continue
    if palabras [0] != "From" : continue
    if len(palabras)>3 : continue
    print(palabras[2])
