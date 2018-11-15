from django.db import models
from user_profile.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from froala_editor.fields import FroalaField


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = FroalaField()
    date = models.DateField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    voters = models.ManyToManyField(Profile)
    likes = models.IntegerField(default=0, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('post_page', kwargs={'post_id': self.id})
