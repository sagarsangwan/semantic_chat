from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse


class ChatRoomManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        return self.get_queryset().filter(lookup).distinct()


class ChatRoom(models.Model):
    first_person = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='first_person', null=True, blank=True)
    second_person = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='second_person', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    objects = ChatRoomManager()

    class Meta:
        unique_together = ('first_person', 'second_person')

    def get_absolute_url(self):
        return reverse('chat:chat_room', kwargs={'slug': self.slug})

    def __str__(self):
        return self.first_person.username + ' - ' + self.second_person.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.first_person.username + '-' + \
                self.second_person.username + '-' + str(self.pk)
        super(ChatRoom, self).save(*args, **kwargs)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.user.username + self.room.slug + str(self.pk)
        super(Message, self).save(*args, **kwargs)
