number_list = []

while True:
    value = input("Ingresa un numero: ")
    try:
        number = int(value)
        number_list.append(number)
    except:
        if value == "hecho":
            print("Maximo: %g" % (max(number_list)))
            print("Minimo: %g" % (min(number_list)))
            quit()
        else:
            print("Valor invalido")

