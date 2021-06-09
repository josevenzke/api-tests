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

def string_to_array(string):
    try:
        arrayOfStrings = string.split(",") 
        arrayOfIntegers = [int(i) for i in arrayOfStrings]
    except:
        return []

    return arrayOfIntegers

def string_to_int(string):
    try:
        integer = int(string)
    except:
        integer = 0
    
    return integer