from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    about = models.CharField(max_length=80)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.email

