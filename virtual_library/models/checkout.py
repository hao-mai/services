from django.db import models
from .book import Book
from .user import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['book']

    def __str__(self):
        return f"{self.user.email} checked out {self.book.title}"

@receiver(post_save, sender=Checkout)
def update_book_availability(sender, instance, created, **kwargs):
    if created:
        book = instance.book
        book.quantity -= 1
        book.save()
        
        if book.quantity == 0:
            book.is_available = False
            book.save()
    elif not created and instance.return_date is not None:
        book = instance.book
        book.quantity += 1
        book.save()

        if book.is_available == False:
            book.is_available = True
            book.save()