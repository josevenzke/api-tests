from .models import ModifyStr
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ModifySerializer
from modifystr import serializers


# Create your views here.
@api_view(['GET'])
def ModifyUrls(request):
    url_patterns = {
        'string_list': 
            {
            'path': '/modify/string-list/',
            'description': 'list all the strings ever made/modified',
            'documentation': 'url_here'
            }
        }

    return Response({'endpoints':url_patterns})


@api_view(['GET'])
def StringList(request):
    method = request.GET.get('method')
    
    kw = {}
    if method:
        kw['method'] = method

    queryset = ModifyStr.objects.filter(**kw)
    serializer = ModifySerializer(queryset,many=True)

    return Response({'Success':True,'string_list':serializer.data,'method':method})

@api_view(['POST'])
def StringReverse(request):
    case_sensitive = request.POST.get('case_sensitive')
    string = request.POST.get('string')

    if case_sensitive:
        string = string.lower()

    reversed = string[::-1]

    modified = ModifyStr.objects.create(original_string=string,new_string=reversed,method='Reverse')
    modified.save()

    serializer = ModifySerializer(modified,many=False)

    return Response({'Success':True,'reversed':reversed,'object':serializer.data})

@api_view(['POST'])
def StringRandomize(request):
    case_sensitive = request.POST.get('case_sensitive')
    string = request.POST.get('string')

    if case_sensitive:
        string = string.lower()

    randomized = ''.join(random.sample(string,len(string)))

    modified = ModifyStr.objects.create(original_string=string,new_string=randomized,method='Randomize')
    modified.save()

    serializer = ModifySerializer(modified,many=False)

    return Response({'Success':True,'randomized':randomized, 'object':serializer.data})

@api_view(['POST'])
def StringSpace(request):
    case_sensitive = request.POST.get('case_sensitive')
    string = request.POST.get('string')
    char = request.POST.get('char')
    if not all([char,string]):
        return Response({'Success':False,'Error':'Missing params'})

    if char not in string:
        return Response({'Success':False,'Error':'Cant find any char in string'})

    spaced_string = string.replace(char," ")

    modified = ModifyStr.objects.create(original_string=string,new_string=spaced_string,method='Space')
    modified.save()

    serializer = ModifySerializer(modified,many=False)

    return Response({'Success':True,'spaced':spaced_string,'object':serializer.data})

