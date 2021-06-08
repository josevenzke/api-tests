from rest_framework.decorators import api_view
from rest_framework.response import Response

from lib import binarysearch_helper
# Create your views here.

@api_view(['POST'])
def binary_search(request):
    array = request.POST.get('array').split(",")
    item = request.POST.get('item')
    array = [int(i) for i in array]


    item = int(item)

    index = binarysearch_helper.search(array,item)

    return Response({'item_index':index})



