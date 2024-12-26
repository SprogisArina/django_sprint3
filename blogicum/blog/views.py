from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def post_detail(request, post_id):
    try:
        posts_by_id[post_id]
    except KeyError:
        raise Http404('Page does not exist')
    return render(request, 'blog/detail.html')


def category_posts(request, category_slug):
    return render(
        request, 'blog/category.html')
