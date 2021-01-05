from django.shortcuts import render, get_object_or_404
from .models import Post


def showblog(request):
    posts = Post.objects
    # Не забываем что у нас html страница в подпапке blog
    # чтобы небыло конфликта имен с файлами
    # из других приложений, теперь можно иметь blog.html в каждом приложении.
    return render(request, 'blog/blog.html', {'posts': posts})


def specific_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/specific_post.html', {'post': post})
