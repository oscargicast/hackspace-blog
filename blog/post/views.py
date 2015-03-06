from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Post

def home(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render_to_response(
        'home/landing.html',
        ctx,
        RequestContext(request),
    )