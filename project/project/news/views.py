from django.forms import DateField, ModelForm
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime




class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['time_now'] = datetime.utcnow()

        context['next_sale'] = None
        return context


class PostDetail(DetailView):

    model = Post
    template_name = 'flatpages/new.html'
    context_object_name = 'new'


class PostsDetail(View):
    def get(self, request, pk):
        ps = Post.objects.get(id=pk)
        return render(request, "flatpages/post.html", {'ps': ps})

    # def get(self, request, pk):
    #     ps = Post.objects.get(id=pk)
    #     return render(request, "flatpages/post.html", {'ps':ps})

    # def news_page_list(request):
    #
    #     newslist = Post.objects.all().order_by('-rating')[:6]
    #
    #     return render(request, 'flatpages/news.html', {'newslist': newslist})