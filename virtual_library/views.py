from rest_framework import viewsets
from virtual_library import models as Library
from serializers import LibrarySerializer
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as django_filters

class LibraryFilterSet(django_filters.FilterSet):
    class Meta:
        model = Library
        fields = ['title', 'author', 'genre', 'year']


class LibraryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated]
    filterset_class = LibraryFilterSet
    ordering = ['title']
    ordering_fields = ['title', 'author', 'genre', 'year']
    search_fields = ['title', 'author', 'genre', 'year']

