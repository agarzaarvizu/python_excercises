import re

filename = input("Ingresa un nombre de archivo: ")
counter = 0
acum = 0

try:
    document = open(filename)
    for linea in document:
        linea = linea.rstrip()
        x = re.findall("New Revision: ([0-9.]+)", linea)
        if len(x) > 0:
            for value in x:
                acum = acum + float(value)
                counter = counter + 1
    print(acum/counter)

except Exception as Error:
    print(Error)


