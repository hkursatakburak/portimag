from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView
from topics.models import Topic


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['topics'] = Topic.objects.filter(available = True).order_by("-date")[:2]
     return context
    

#def index(request):
#    return render(request, 'index.html')

class HakkımdaView(TemplateView):
    template_name = 'hakkımda.html'

#def hakkımda(request):
#    return render(request, 'hakkımda.html')