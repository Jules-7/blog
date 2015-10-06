from django.contrib import admin
from blog.models import Category, Post, Comment


class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'admin_image', 'category', 'pub_date', 'expire_date', 'is_active', 'like')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = 'admin_image'



class CategoryAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
