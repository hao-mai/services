from rest_framework import viewsets
from virtual_library import models as Library
from serializers import LibrarySerializer
from rest_framework.permissions import IsAuthenticated


class LibraryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated]


    