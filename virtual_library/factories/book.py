import factory
from virtual_library.models import Book

class BookFactory(factory.Factory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    author = factory.Faker('name')
    description = factory.Faker('paragraph')
    num_pages = factory.Faker('random_int', min=50, max=500)
    available = True
    quantity = 10
