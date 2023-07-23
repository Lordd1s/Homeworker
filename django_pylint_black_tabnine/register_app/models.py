from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=35)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        app_label = "register_app"
        ordering = ("username",)
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
