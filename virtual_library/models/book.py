from django.db import models

class Genre(models.Model):
    """
    Genre of the book
    """
    name = models.CharField(max_length=255)


class Book(models.Model):
    """
    Library that will store and manage books
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)
    num_pages = models.IntegerField()
    available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["title"]
        verbose_name = "Book"
        verbose_name_plural = "Books"
        default_permissions = ("add", "change", "delete", "view")

    def save(self, *args, **kwargs):
        if self.quantity > 0:
            self.is_available = True
        else:
            self.is_available = False
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)
