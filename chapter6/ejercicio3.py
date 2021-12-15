def cuenta(palabra, buscar_letra):
    contador = 0
    palabra = palabra.lower()
    for letra in palabra:
        if letra == buscar_letra:
            contador = contador + 1
    return contador


palabra = input("Ingresa una cadena: ")
buscar_letra = input("Ingresa la letra a contar: ")
contador = cuenta(palabra, buscar_letra)
print(contador)
