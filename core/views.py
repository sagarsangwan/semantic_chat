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
    first_person = current_user
    second_person = user

    lookup1 = Q(first_person=first_person) & Q(second_person=second_person)
    lookup2 = Q(first_person=second_person) & Q(second_person=first_person)
    lookup = Q(lookup1 | lookup2)

    chat_room = ChatRoom.objects.filter(lookup).first()
    if chat_room is None:
        chat_room = ChatRoom.objects.create(
            first_person=first_person, second_person=second_person)
        created = True
    else:
        created = False

    if created:
        print('Chat room created', chat_room.slug)
    else:
        print('Chat room already exists', chat_room.slug)
    return redirect('chat:chat_room', slug=chat_room.slug)


def chat_room(request, slug):
    room = ChatRoom.objects.get(slug=slug)
    print(room.first_person.username, 'first person')
    print(room.second_person.username, 'second person')

    context = {
        'room': room
    }
    return render(request, 'pages/chat-room.html', context)


def search_people(request):
    return render(request, 'pages/search-people.html')
