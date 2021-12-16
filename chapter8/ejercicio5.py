filename = input("Ingresa un nombre de archivo: ")
contador = 0

try:
    manejador = open(filename)
    for linea in manejador:
        linea = linea.rstrip()
        if linea.startswith("From"):
            list_words = linea.split(" ")
            if list_words[0] != "From:":
                contador = contador + 1
                print(list_words[1])

    print("Hay %d lineas en el archivo con la palabra From al inicio" % contador)
except:
    print("nombre de archivo invalido")
