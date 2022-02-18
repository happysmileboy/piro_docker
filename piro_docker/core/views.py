from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.models import Post


def hello_world(request: HttpRequest):
    post, _ = Post.objects.get_or_create(title='hi')
    post.count += 1
    post.save()
    count = post.count
    need_count = 10 - count
    if need_count > 0:
        return HttpResponse(f'Hello World! Your count is {post.count}. plz enter {need_count} more!')
    else:
        post.count = 0
        post.save()
        return HttpResponse(f'Hello World! Your count is {count}. Thank you')
