from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_list, name = "topics"),
    path('<slug:category_slug>/<int:topic_id>', views.topic_detail, name = "topic_detail"),
    path('categories/<slug:category_slug>', views.category_list, name = "topic_by_category"),
    path('tags/<slug:tag_slug>', views.tag_list, name = "topic_by_tag"),

]