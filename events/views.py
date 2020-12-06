from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'events/home.html') # Поместили файл в подпапку чтобы небыло конфликта имен с файлами
    # из других приложений, теперь можно иметь home.html в каждом приложении.