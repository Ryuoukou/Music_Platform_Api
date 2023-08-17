import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ] #Выбор пола из 3 предложенных
    email = models.EmailField(unique=True) #Поле для email
    name = models.CharField(max_length=100) #Поле для имя пользователя
    password = models.CharField(max_length=128) #Поле для пароля
    birth_date = models.DateField(default=datetime.date(1900, 1, 1)) #Поле для даты рождения с дефолтной датой 1900,1,1
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)#Само поле для пола с возможностью выбора только из GENGER_CHOICE
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=False)

    def __str__(self):
        return self.name #При обращении к моей модели CustomUser будет возвращено именно username


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=150, default='')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=150) #Название трека
    duration = models.DurationField() #Длительность трека
    file = models.FileField(upload_to='tracks/') #Поле для хранения трека с указанной папкой для хранения
    album = models.ForeignKey(Album, on_delete=models.CASCADE) #Связь трека с Альбомом к которому он привязан

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField(max_length=200)
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.title
