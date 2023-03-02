from virtual_library.models import Book
from django.shortcuts import render

def book_view(request):
        books = Book.objects.all()
        context = {"books": books}
        return render(request, 'virtual_library/book.html', context=context)