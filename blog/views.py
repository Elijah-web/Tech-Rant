from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.

class HomeView(generic.ListView):
	template_name = 'blog/home.html'
	model = Post
	context_object_name = 'posts'
	
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['title'] = "&C"
    #     return context

class DetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = Post
    context_object_name = 'post'