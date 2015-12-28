from blog.models import Comment
from django import template


register = template.Library()

@register.simple_tag
def number_of_comments(post_id):
    return len(Comment.objects.filter(post=post_id))
