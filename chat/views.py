from django.shortcuts import render

from .models import Room

def index(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})

def room_detail(request, room_name):
    room = Room.objects.get(name=room_name)
    return render(request, 'chat/room.html', {'room': room})