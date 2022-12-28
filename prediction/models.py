from django.db import models

class Traduction(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    texte = models.CharField(max_length=50, null=True)
    date = models.DateField(auto_now_add = True)
