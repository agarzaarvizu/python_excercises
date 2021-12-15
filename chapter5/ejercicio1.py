total = 0
n = 0
mean = 0

while True:
    value = input("Introduzca un numero: ")
    if value == "fin":
        break
    else:
        try:
            valor = int(value)
            total = total + valor
            n = n + 1
            mean = total / n
        except:
            print("Entrada invalida") 

print(total, n, mean)
