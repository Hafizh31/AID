from django.db import models


class Penyakit(models.Model):
    jenispenyakit = models.CharField(max_length=100)
    penyebab = models.CharField(max_length=10000)
    pencegahan = models.CharField(max_length=10000)
