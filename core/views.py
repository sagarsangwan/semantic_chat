from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import User, ChatRoom, Message, ChatRoomManager
from django.db.models import Q
# def login(request):
#     return render(request, 'landing_page/login.html')


@login_required
def home(request):
    search = request.GET.get('search')
    current_user = request.user
    if search:
        all_users = User.objects.filter(
            Q(username__icontains=search) | Q(email__icontains=search))
        all_users = all_users.exclude(username=current_user.username)

        all_users = all_users.exclude(is_superuser=True)
        print(all_users)
        context = {
            'all_users': all_users
        }
        return render(request, 'pages/search_result.html', context)
    all_chat_rooms = ChatRoom.objects.by_user(user=request.user)
    print(all_chat_rooms)
    context = {
        'all_chat_rooms': all_chat_rooms
    }
    return render(request, 'home.html', context)


def new_chat_room(request, user_id):
    print(user_id)
    current_user = request.user
    user = User.objects.get(pk=user_id)
    # check if chat room already exists

    chat_room, created = ChatRoom.objects.get_or_create(
        Q(first_person=current_user, second_person=user) | Q(first_person=user, second_person=current_user))

    if created:
        print('Chat room created')
    else:
        print('Chat room already exists')
    return redirect('chat:chat_room', room_name=chat_room.slug)


def chat_room(request, slug):
    room = ChatRoom.objects.get(slug=slug)
    room_name = room.slug
    context = {
        'room_name': room_name
    }
    return render(request, 'pages/chat-room.html', context)


def search_people(request):
    return render(request, 'pages/search-people.html')
