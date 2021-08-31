from django.contrib import admin
from .models import Post

# Register your models here.


# From build a blog app with django tutorial
# Organize the admin display for blog posts
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)