from django.db import models
from .MemberLevels import MemberLevels
from .ParanoiaLevels import ParanoiaLevels

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=60)
    email = models.EmailField()
    passkey = models.CharField(max_length=60)

    account_locked = models.BooleanField(default=False)

    joined_date = models.DateField(auto_now_add=True) 

    uploaded = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    downloaded = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    torrents_uploaded = models.IntegerField(default=0)
    torrents_downloaded = models.IntegerField(default=0)

    member_type = models.IntegerField(default=MemberLevels.Member.value)
    paranoia_level = models.IntegerField(default=ParanoiaLevels.High.value)

    invites = models.IntegerField(default=0)
    can_invite = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class UserLogin(models.Model):
    user = models.ForeignKey(User)
    login = models.DateTimeField()
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.user.username

class Torrent(models.Model):
    uploader = models.ForeignKey(User)

    title = models.CharField(max_length=100)
    description = models.TextField()
    size = models.DecimalField(max_digits=6,decimal_places=2, default=0)

    date_uploaded = models.DateTimeField(auto_now_add=True)

    downloads = models.IntegerField(default=0)

    seeders = models.IntegerField(default=0)
    leechers = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Report(models.Model):
    reporter = models.ForeignKey(User)
    reported_torrent = models.ForeignKey(Torrent)
    reason = models.TextField()

class Tag(models.Model):
    creator = models.ForeignKey(User)
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag

class TorrentTag(models.Model):
    torrent = models.ForeignKey(Torrent)
    tag = models.ForeignKey(Tag)

    def __str__(self):
        return self.tag
