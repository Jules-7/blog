from django.conf.urls import include, url
from blog.views import CategoriesListView, PostsListView, CategoriesDetailView, PostsDetailView

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^category/$', CategoriesListView.as_view(), name="categories_list"),
    url(r'^post/$', PostsListView.as_view(), name="posts_list"),

    url(r'^category/(?P<slug>[-\w]+)$', CategoriesDetailView.as_view(), name="category_detail"),
    url(r'^post/(?P<slug>[-\w]+)$', PostsDetailView.as_view(), name="post_detail"),
]
