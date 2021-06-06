from .models import Person
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer

@api_view(['GET'])
def PersonList(request):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all()
    serialize = PersonSerializer(queryset,many=True)

    return Response(serialize.data)


@api_view(['POST'])
def PersonCreate(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    person = Person.objects.create(first_name=first_name,last_name=last_name)
    
    serializer = PersonSerializer(person,many=False)

    return Response(serializer.data)