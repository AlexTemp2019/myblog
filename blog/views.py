from django.shortcuts import render
from .models import Post


def showblog(request):
    posts = Post.objects
    # Не забываем что у нас html страница в подпапке blog
    # чтобы небыло конфликта имен с файлами
    # из других приложений, теперь можно иметь blog.html в каждом приложении.
    return render(request, 'blog/blog.html', {'posts': posts})
