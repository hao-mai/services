from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from virtual_library.models import Checkout, Book
from virtual_library.serializers import CheckoutSerializer
from rest_framework.decorators import action

class CheckoutViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to checkout books.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CheckoutSerializer

    def create(self, request):
        book_id = request.data.get('book_id', None)
        user_id = request.user.id

        # Check if book is available
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

        if not book.is_available:
            return Response({'error': 'Book is not available.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create checkout
        checkout = Checkout(book=book, user_id=user_id)
        checkout.save()

        # Update book availability
        book.quantity -= 1
        if book.quantity == 0:
            book.is_available = False
        book.save()

        # Return checkout details
        serializer = CheckoutSerializer(checkout)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        checkouts = Checkout.objects.filter(user=request.user)
        serializer = CheckoutSerializer(checkouts, many=True)
        return Response(serializer.data)
    

    @action(detail=True, methods=['post'], name='return_early')
    def return_early(self, request, pk=None):
        checkout = self.get_object()
        # Handle "return book early" functionality here
        return Response({'message': 'Book returned early'})
