from django.shortcuts import render
from .models import Event

# Create your views here.
def home(request):
    events = Event.objects
    return render(request, 'events/home.html', {'events': events}) # Поместили файл в подпапку events/ чтобы небыло конфликта имен с файлами
    # из других приложений, теперь можно иметь home.html в каждом приложении.

