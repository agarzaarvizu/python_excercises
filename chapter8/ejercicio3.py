manejador = open("../files/mbox-short.txt")
contador = 0

for linea in manejador:
    palabras = linea.split()
    if len(palabras)==0 or len(palabras)>3 or (palabras [0] != "From"):
        continue
    else:
        print(palabras[2])
