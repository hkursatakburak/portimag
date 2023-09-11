from django.urls import path
#from . import views
from pages.views import HakkımdaView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name = "index"),
    path('hakkımda/', HakkımdaView.as_view(), name = "hakkımda")
    
]
