from rest_framework.exceptions import APIException


def string_to_array(string):
    try:
        arrayOfStrings = string.split(",") 
        arrayOfIntegers = [int(i) for i in arrayOfStrings if i.isdigit()]
        if not arrayOfIntegers:
            raise APIException({'detail': 'Parametros invalidos', 'exception': e})
            
    except Exception as e:
        raise APIException({'detail': 'Parametros invalidos', 'exception': e})
        
    return arrayOfIntegers

def string_to_int(string):
    try:
        integer = int(string)
    except Exception as e:
        return APIException({'detail': 'Parametros invalidos','exception':e})
        
    
    return integer