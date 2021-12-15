filename = input("Ingresa un nombre de archivo: ")
n = 0
mean = 0
total = 0

try:
    man_a = open(filename)
    for line in man_a:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence"):
            index = line.find(":")
            total = total + float(line[index + 1:])
            n = n + 1
        else:
            continue
    print("Promedio spam confidence: ", (total / n))
except:
    print("Nombre de archivo invalido: ", filename)
