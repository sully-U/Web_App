
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the register index.")


def homepage(request):
    return render(request, 'homepage.html')

def thanks(request):
    context = {}
    firstname = request.POST.get('firstname', None)
    context['firstname']= firstname
    return render(request, 'thanks.html', {'firstname': firstname})

def register(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
