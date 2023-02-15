from django.db import models

class Publisher(models.Model):
    """
    Publisher of the book
    """
    name = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    published_date = models.DateField()

class Genre(models.Model):
    """
    Genre of the book
    """
    name = models.CharField(max_length=255)
    description = models.TextField()


class Book(models.Model):
    """
    Library that will store and manage books
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,related_name="publisher")
    genres = models.ManyToManyField(Genre)
    num_pages = models.IntegerField()
    availabiity = models.BooleanField()

    class Meta:
        ordering = ["title"]
        verbose_name = "Book"
        verbose_name_plural = "Books"
        default_permissions = ("add", "change", "delete", "view")

    def __str__(self):
        return str(self.title)
