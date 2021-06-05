from .models import Person
from rest_framework import viewsets
from teste.serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.values()
    serializer_class = PersonSerializer