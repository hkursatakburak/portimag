from django.contrib import admin
from . models import Topic, Category, Tag
# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name", "available")
    list_filter = ("available",)
    listfield = ("name", "desciription")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('name',)} #slug alanını name alanından aldıdık 

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('name',)} 