from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify
from django.urls import reverse

class Room(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(blank=True) 
    online = models.ManyToManyField(to=User, blank=True)

    def add_user_to_online(self, user):
        if user not in self.online.all():
            self.online.add(user)
            self.save()

    def remove_user_from_online(self, user):
        if user in self.online.all():
            self.online.remove(user)
            self.save()

    def get_online_users(self):
        return self.online.all()


    
    def get_absolute_url(self):
        return reverse("chat:room_view",kwargs={"room_name":self.slug})
    @property
    def data(self):
        return self.message_set.all()

    def save(self, *args,**kwargs) -> str:
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.name} ({self.online.count()} online)'  

class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]'