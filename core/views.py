from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.


# def login(request):
#     return render(request, 'landing_page/login.html')


@login_required
def home(request):
    return render(request, 'home.html')


def chat_room(request, room_name):
    print(room_name)
    context = {
        'room_name': room_name
    }
    return render(request, 'pages/chat-room.html', context)
