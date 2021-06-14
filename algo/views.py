import time

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException


from lib import binarysearch_helper as binary
from lib import quicksort_helper as quicksort
from lib import converter_helper as converter

# Create your views here.

@api_view(['POST'])
def binary_search(request):
    arrayString = request.POST.get('array')
    itemString = request.POST.get('item')
    
    if not all([arrayString,itemString]):
        raise APIException({'detail':'Parametros insuficientes'})
    
    array = converter.string_to_array(arrayString)
    item = converter.string_to_int(itemString)
    
    index = binary.search(array,item)
    
    return Response({'Success':False ,'item_index':index,'array_lenght':len(array)})

@api_view(['POST'])
def quicksort_sort(request):
    arrayString = request.POST.get('array')
    
    if not arrayString:
        raise APIException({'detail':'Parametros insuficientes'})
    
    array = converter.string_to_array(arrayString)

    startTime = time.process_time()
    sortedArray = quicksort.sort(array)
    timeTaken = time.process_time() - startTime,'seconds'

    return Response({'Success':True,'original_array': array,'sorted_array':sortedArray,'time_taken':timeTaken})
