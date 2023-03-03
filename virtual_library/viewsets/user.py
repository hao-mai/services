from rest_framework import viewsets
from virtual_library.serializers import UserSerializer
from virtual_library.models import User


class UserViewSet(viewsets.ModelViewSet):
    """A very basic create-only viewset for users. 
    Further functionality such as email verification, password reset, etc. 
    will be implemented at another time. """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)


