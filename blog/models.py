from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="category title")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('slug',)

    def __unicode__(self):
        return '%s' % self.title

    #@permalink
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="post title")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="slug")
    #content = tinymce_models.HTMLField(verbose_name="post content")
    content = RichTextField()
    pub_date = models.DateTimeField(verbose_name="date of posting")
    expire_date = models.DateTimeField(verbose_name="date of post expire")
    is_active = models.BooleanField(default=True, verbose_name="show post")
    category = models.ForeignKey(Category, related_name='posts', verbose_name="category")
    user = models.ForeignKey(User, related_name="posts", verbose_name="user")
    like = models.IntegerField(default=0, verbose_name="likes")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ('slug',)

    def __unicode__(self):
        return '%s' % self.title

    #@permalink
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    post = models.ForeignKey(Post, related_name="comments", verbose_name="post")
    text = models.TextField(max_length=500, verbose_name="comment")
    pub_date = models.DateTimeField(verbose_name="date of posting")
    allowed = models.BooleanField(default=False, verbose_name="approved by admin")
    like = models.IntegerField(default=0, verbose_name="likes")

    def __unicode__(self):
        return self.text

    class Meta:
        app_label = "bla"

