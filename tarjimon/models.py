from django.db import models

class Lugat(models.Model):
    inglizcha  = models.CharField ('Inglizcha', max_length=30)
    uzbekcha = models.CharField('Uzbekcha', max_length=30)
