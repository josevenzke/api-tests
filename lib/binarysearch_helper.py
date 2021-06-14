
def search(array, item):
    baixo = 0
    alto = len(array) - 1
    meio = 0

    while baixo <= alto: 
        meio = (alto + baixo) // 2
        
        if array[meio] < item:
            baixo = meio + 1 
        elif array[meio] > item:
            alto = meio - 1 
        else:
            return meio
    
    return -1
