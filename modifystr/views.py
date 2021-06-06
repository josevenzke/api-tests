from .models import ModifyStr
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ModifySerializer
from modifystr import serializers

# Create your views here.
@api_view(['GET'])
def StringList(request):
    queryset = ModifyStr.objects.all()
    serializer = ModifySerializer(queryset,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def StringReverse(request):
    case_sensitive = request.POST.get('case_sensitive')
    string = request.POST.get('string')

    if case_sensitive:
        string = string.lower()

    reversed_string = string[::-1]
    modified = ModifyStr.objects.create(original_string=string,new_string=reversed_string,method='Reverse')
    modified.save()

    serializer = ModifySerializer(modified,many=False)

    return Response({'Success':True,'reversed':reversed_string,'object':serializer.data})

@api_view(['POST'])
def StringRandomize(request):
    case_sensitive = request.POST.get('case_sensitive')
    string = request.POST.get('string')

    if case_sensitive:
        string = string.lower()

    randomized_string = ''.join(random.sample(string,len(string)))
    modified = ModifyStr.objects.create(original_string=string,new_string=randomized_string,method='Randomize')
    modified.save()

    serializer = ModifySerializer(modified,many=False)

    return Response({'Success':True,'randomized':randomized_string, 'object':serializer.data})