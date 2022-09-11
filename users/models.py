from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    model of users of I-NET Shop MTS
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    persnumber = models.CharField(max_length=14, unique=True)
    telnumber = models.CharField(max_length=12, unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'