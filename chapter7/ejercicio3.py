filename = input("Ingresa un nombre de archivo: ")
n = 0
mean = 0
total = 0

try:
    man_a = open(filename)
    for line in man_a:
        line = line.rstrip()
        if line.startswith("Subject:"):
            n = n + 1
        else:
            continue
    print("Hay %d lineas subject en %s" % (n,filename))
except:
    if filename.lower() == "na na boo boo":
        print("NA NA BOO BOO PARA TI - Te he atrapado!")
    else:
        print("Nombre de archivo invalido: ", filename)
