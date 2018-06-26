from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField()
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    user_who_posted = models.ForeignKey('User', on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'User', related_name='user_who_followed', blank=True)
    user_who_liked = models.ManyToManyField(
        'User', related_name='user_who_liked', blank=True)
    user_who_disliked = models.ManyToManyField(
        'User', related_name='user_who_disliked', blank=True)
    located = models.ForeignKey('Location', on_delete=models.CASCADE)
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE, blank=True)


class Mood(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()


class comment(models.Model):
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    user_who_made = models.ForeignKey('User', on_delete=models.CASCADE)
    which_post = models.ForeignKey('Post', on_delete=models.CASCADE)
