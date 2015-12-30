from django.contrib import admin
from .models import Comment
from .models import Page
from .models import Post

admin.site.register(Comment)
admin.site.register(Page)
admin.site.register(Post)
