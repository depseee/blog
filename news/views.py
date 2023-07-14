from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView


# Create your views here.

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsCreateView(CreateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'news/create.html'
    success_url = '/news'


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'news/update.html'
    success_url = '/news'


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete.html'
    success_url = '/news'
