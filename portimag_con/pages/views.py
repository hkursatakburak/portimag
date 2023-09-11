from django.http import HttpResponse
from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from . forms import ContactForm
from topics.models import Topic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


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



class ContactView(SuccessMessageMixin,FormView):
   template_name = 'contact.html'
   form_class = ContactForm
   success_url = reverse_lazy('contact')  #başarılı bir post işleminden sonra ilk sayfaya yönlendirdik
   success_message = 'Yanıtınız başarıyla gönderildi'

   def form_valid(self, form):  #formu kaydettik
        form.save()
        return super().form_valid(form)
      
       