filename = input("Ingresa nombre de archivo: ")
manejador = open(filename)
checker = []

for line in manejador:
    list_words = line.split()
    for word in list_words:
        if not word in checker:
            checker.append(word)

checker.sort()
print(checker)
