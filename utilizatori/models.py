from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Utilizatori(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nume = models.CharField(max_length=100)
    description = models.TextField()
    cnp = models.BigIntegerField(null=True)
    img = models.ImageField(upload_to='media/pictures')
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.nume
