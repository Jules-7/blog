from django.shortcuts import render, redirect
#from django.views.generic import ListView, DetailView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from blog.forms import SearchForm
from blog.models import Category, Post
from taggit.models import Tag, TaggedItem


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


def show_posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name__in=[tag_name])
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag_name': tag_name})

def tags(request):
    tags_dict = {}
    tags_list = Tag.objects.all()
    for each in tags_list:
        tag = Tag.objects.get(id=each.id)
        tag_num = TaggedItem.objects.filter(tag_id=tag.id).count()
        tags_dict[each] = tag_num
    return render(request, 'blog/tags.html', {'tags_dict': tags_dict})
