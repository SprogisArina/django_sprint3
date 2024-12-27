from datetime import datetime

from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def index(request):
    post_list = Post.objects.select_related('location').filter(
        pub_date__lte=datetime.now(),
        is_published=True,
        category__is_published=True
    )[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(Post.objects.filter(
        pub_date__lte=datetime.now(),
        is_published=True,
        category__is_published=True),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True, slug=category_slug)
    )
    post_list = Post.objects.filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__lte=datetime.now(),
        category__is_published=True
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
