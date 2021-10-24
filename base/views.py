from django.shortcuts import render
from .models import Room
# Create your views here.

# rooms = [
#     {'id': 1, 'name':'Lets learn Python!'},
#     {'id': 2, 'name':'Lets learn ReactJS!'},
#     {'id': 3, 'name':'Lets learn Node!'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = { 'room': room} 
    return render(request, 'base/room.html', context)