from django.contrib import admin

# Register your models here.
from .models import Comment
from .models import Page
from .models import Post

admin.site.register(Comment)
admin.site.register(Page)
admin.site.register(Post)
