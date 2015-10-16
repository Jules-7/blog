from django.shortcuts import render
#from django.views.generic import ListView, DetailView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from blog.models import Category, Post


class CategoriesListView(ListView):
    model = Category
    fields = '__all__'
    template_name = 'blog/category_list.html'


class PostsListView(ListView):
    model = Post
    fields = '__all__'


class CategoriesDetailView(DetailView):
    model = Category
    fields = '__all__'
    context_object_name = 'category'


class PostsDetailView(DetailView):
    model = Post
    fields = '__all__'
    context_object_name = 'post'
