from django.db import models
from django.utils import timezone


# Create your models here.
class Something(models.Model):
    id = models.IntegerField(primary_key=True)
    something = models.TextField()
    title = models.CharField(max_length=50)
    date_time = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    class Meta:
        app_label = "ORM_train"
        ordering = ("-date_time", "title")
        verbose_name = "Something"
        verbose_name_plural = "Somethings"

    def __str__(self):
        return f"{self.title}"
