
def sort(lista):
    if len(lista) <2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i <=pivo]
        maiores = [i for i in lista[1:] if i > pivo]

        return sort(menores) + [pivo] + sort(maiores)

