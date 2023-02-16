from rest_framework import serializers
from virtual_library import models as Library

class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = ['title', 'author', 'genre', 'year']
