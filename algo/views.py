from rest_framework.decorators import api_view
from rest_framework.response import Response

from lib import binarysearch_helper as binary
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
        index = []
        
    return Response({'item_index':index,'array_lenght':len(array)})



