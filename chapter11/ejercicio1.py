import re

man = open("../files/mbox.txt")
coincidencias = list()
expresion = input("Ingresa una expresion regular: ")

for linea in man:
    linea = linea.rstrip()
    x = re.findall(expresion, linea)
    if len(x) > 0:
        coincidencias = coincidencias + x

print("mbox.txt tiene %d lineas que coinciden con %s" % (len(coincidencias),expresion))

