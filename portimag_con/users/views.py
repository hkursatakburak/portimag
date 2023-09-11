from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from users.models import User
from topics.models import Topic

class UserListView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = "user.html"
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topics"] = Topic.objects.filter(available=True, user = self.kwargs['pk'])
        return context


