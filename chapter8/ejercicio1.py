def recortar(lista):
    del lista[0]
    del lista[len(lista) - 1]

def medio(lista):
    lista2 = lista[1:(len(lista)-1)]
    return lista2

lista = [5, 4, 3, 2, 1]
recortar(lista)
print(lista)
lista2 = [8, 7, 6, 5, 4, 3]
lista2 = medio(lista2)
print(lista2)

