from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    period_play = models.CharField(max_length=2000)
    description = models.TextField(max_length=200000)
    image_url = models.CharField(max_length=2083)

