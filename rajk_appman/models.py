from django.db import models


class App(models.Model):

    id = models.CharField(max_length=25, primary_key=True)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
