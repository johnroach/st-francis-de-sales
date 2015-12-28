from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    date = models.DateField('date published')
    time = models.TimeField()
    creation_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    title = models.TextField(max_length=255)
    text = models.TextField()
    slug = models.TextField(max_length=255)
    modified_by = models.ForeignKey(User, related_name="post_modified_by")
    created_by = models.ForeignKey(User, related_name="post_created_by")

    def __str__(self):
        return self.title

class Comment(models.Model):
    date = models.DateField('date published')
    creation_time = models.DateTimeField()
    email = models.EmailField()
    name = models.CharField(max_length=25)
    parent = models.ForeignKey("self", related_name="parent_comment",
        default=None, null=True, blank=True)
    post = models.ForeignKey(Post, related_name="parent_post")
    comment = models.TextField(max_length=2000)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.comment[:255]

class Page(models.Model):
    title = models.TextField(max_length=255)
    slug = models.TextField(max_length=255)
    text = models.TextField()
    rank = models.IntegerField()
    creation_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    modified_by = models.ForeignKey(User, related_name="page_modified_by")
    created_by = models.ForeignKey(User, related_name="page_created_by")

    def __str__(self):
        return self.title
