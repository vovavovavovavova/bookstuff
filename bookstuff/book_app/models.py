from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class SupportStuff(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    note = models.TextField(null=True)


class Book(models.Model):
    author = models.CharField(max_length=100, null=False)
    title = models.TextField(null=False)
    currency = models.CharField(max_length=5)
    language = models.CharField(max_length=20)
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    

    
class Offer(models.Model):
    title = models.CharField(max_length=50, null=False)
    data = models.JsonField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)


class OfferResolve(models.Model):
    status = models.TextField(null=False)
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE, null=False)
    support_stuff_id = models.ForeignKey(SupportStuff, on_delete=models.CASCADE, null=False)
