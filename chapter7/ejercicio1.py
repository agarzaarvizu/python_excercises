filename = input("Ingresa un nombre de archivo: ")

try:
    man_a = open(filename)
    for line in man_a:
        line = line.rstrip()
        if not line == "": 
            print(line.upper())
except:
    print("Nombre de archivo invalido: ", filename)
