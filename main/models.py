from django.db import models

# Create your models here.


class Genres(models.Model):
    genre_id = models.IntegerField(null=True, blank=True)
    genre_parent_id = models.IntegerField(null=True, blank=True)
    genre_title = models.CharField(max_length=255, null=True, blank=True)
    genre_handle = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.genre_title

class Artist(models.Model):
    pass


class Albums(models.Model):
    pass


class Tracks(models.Model):  
    pass