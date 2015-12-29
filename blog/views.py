from .helper.query_helper import QuerySetChain
from .models import Comment
from .models import Page
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import functools
import operator


def index(request):

    latest_blog_posts = Post.objects.order_by('-date').all()
    paginator = Paginator(latest_blog_posts, 2)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        'meta_description': 'This is the meta description',
        'page_name': 'home',
        'menu': menu_generator(),
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def single_post(request, year, day, month, url_slug):
    single_post = Post.objects.filter(date=datetime.date(int(year),
        int(month), int(day)), slug=url_slug)

    context = {
        'meta_description': 'This is a meta description',
        'menu': menu_generator(),
        'single_post': single_post,
    }
    return render(request, 'blog/post.html', context)

def search_result(request):
    query = request.GET.get('q')
    if query:
        query_list = query.split()
        all_post_search_results = Post.objects.filter(
            functools.reduce(operator.or_,
                (Q(title__icontains=q) for q in query_list)) |
            functools.reduce(operator.or_,
                (Q(text__icontains=q) for q in query_list))
            )

        all_page_search_results = Page.objects.filter(
            functools.reduce(operator.or_,
                (Q(title__icontains=q) for q in query_list)) |
            functools.reduce(operator.or_,
                (Q(text__icontains=q) for q in query_list))
            )

    all_search_results = QuerySetChain(all_post_search_results,
        all_page_search_results)
    paginator = Paginator(all_search_results, 10)

    page = request.GET.get('page')

    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        search_results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        search_results = paginator.page(paginator.num_pages)

    context = {
        'meta_description': 'This is the meta description',
        'menu': menu_generator(),
        'search_results': search_results,
    }
    return render(request, 'blog/search.html', context)

def slugged_page(request, page_slug):
    pages = Page.objects.filter(slug=page_slug)
    context = {
        'meta_description': 'This is a meta description',
        'menu': menu_generator(),
        'page_name': pages[0].slug,
        'page': pages[0],
    }
    return render(request, 'blog/page.html', context)

def tagged_posts(request, tags):
    return HttpResponse(tags)

def categoried_posts(request, categories):
    return HttpResponse(categories)

def menu_generator():
    pages = Page.objects.order_by('-rank').all()
    return pages
