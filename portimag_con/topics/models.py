from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null= True)
    slug = models.SlugField(max_length=50, unique= True ,null= True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, null= True)
    slug = models.SlugField(max_length=50, unique= True ,null= True)
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="konu adı", help_text="konu başlğı girin")
    category = models.ForeignKey(Category, null=True, on_delete= models.DO_NOTHING)
    tag = models.ManyToManyField(Tag,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to= "topics/%Y/%m/%d/",default= "default.jpg" )
    date = models.DateField(auto_now= True)
    available = models.BooleanField(default= True)
    
    def __str__(self):
        return self.name
