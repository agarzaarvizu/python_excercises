total = 0
n = 0
min_value = 0
max_value = 0
values_list = []

while True:
    value = input("Introduzca un numero: ")
    if value == "fin":
        break
    else:
        try:
            valor = int(value)
            total = total + valor
            n = n + 1
            values_list.append(valor)
            min_value = min(values_list)
            max_value = max(values_list)
        except:
            print("Entrada invalida") 

print(total, n, min_value, max_value)
