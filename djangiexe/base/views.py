from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn Python'},
    {'id':2, 'name':'Waka Waka'},
    {'id':3, 'name':'Frontend developers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')