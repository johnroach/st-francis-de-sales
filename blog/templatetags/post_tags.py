from blog.models import Comment
from django import template
import urllib.parse
import hashlib

register = template.Library()

@register.simple_tag
def number_of_comments(post_id):
    return len(Comment.objects.filter(post=post_id))

@register.simple_tag
def comment_author_gravatar(email):
    size = 65
    # construct the url
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + "?"
    gravatar_url += urllib.parse.urlencode({'d':'identicon', 's':str(size)})
    return gravatar_url
