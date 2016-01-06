from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    created_by = models.ForeignKey(User, related_name="post_created_by")
    creation_time = models.DateTimeField()
    date = models.DateField('date published')
    modified_by = models.ForeignKey(User, related_name="post_modified_by")
    modified_time = models.DateTimeField()
    published = models.BooleanField(default=False)
    slug = models.TextField(max_length=255)
    text = models.TextField()
    time = models.TimeField()
    title = models.TextField(max_length=255)
    disable_comments = models.BooleanField(default=False)
    hide_comments = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    approved = models.BooleanField(default=False)
    comment = models.TextField(max_length=2000)
    creation_time = models.DateTimeField()
    date = models.DateField('date published')
    email = models.EmailField()
    name = models.CharField(max_length=25)
    parent = models.ForeignKey("self", related_name="parent_comment",
        default=None, null=True, blank=True)
    post = models.ForeignKey(Post, related_name="parent_post")

    def __str__(self):
        return self.comment[:255]

class Page(models.Model):
    created_by = models.ForeignKey(User, related_name="page_created_by")
    creation_time = models.DateTimeField()
    modified_by = models.ForeignKey(User, related_name="page_modified_by")
    modified_time = models.DateTimeField()
    published = models.BooleanField(default=False)
    rank = models.IntegerField()
    slug = models.TextField(max_length=255)
    text = models.TextField()
    title = models.TextField(max_length=255)

    def __str__(self):
        return self.title
