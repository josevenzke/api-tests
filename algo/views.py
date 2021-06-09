import time

from rest_framework.decorators import api_view
from rest_framework.response import Response

from lib import binarysearch_helper as binary
from lib import quicksort_helper as quicksort

# Create your views here.

@api_view(['POST'])
def binary_search(request):
    arrayString = request.POST.get('array')
    itemString = request.POST.get('item')
    
    array = binary.string_to_array(arrayString)
    item = binary.string_to_int(itemString)

    if array and item:
        index = binary.search(array,item)
    else:
        return Response({'Success':False})

    return Response({'Success':False ,'item_index':index,'array_lenght':len(array)})

@api_view(['POST'])
def quicksort_sort(request):
    arrayString = request.POST.get('array')

    array = binary.string_to_array(arrayString)

    startTime = time.process_time()
    sortedArray = quicksort.sort(array)
    timeTaken = time.process_time() - startTime,'seconds'

    return Response({'original_array': array,'sorted_array':sortedArray,'time_taken':timeTaken})
