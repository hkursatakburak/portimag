from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="konu adı", help_text="konu başlğı girin")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to= "topics/%Y/%m/%d/",default= "topics/blog_1.jpg" )
    date = models.DateField(auto_now= True)
    available = models.BooleanField(default= True)

def __str__(self):
    return self.name
