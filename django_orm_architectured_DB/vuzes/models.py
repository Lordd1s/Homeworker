from django.db import models


class VuzName(models.Model):
    name = models.TextField(verbose_name="VUZ Name")
    build_date = models.DateField(verbose_name="Build Date")
    location = models.TextField(verbose_name="Location")
    capacity = models.IntegerField()

    class Meta:
        app_label = "vuzes"
        ordering = ("capacity", "-build_date")
        verbose_name = "VUZ Name"
        verbose_name_plural = "VUZ Names"

    def __str__(self):
        return self.name


class Speciality(models.Model):
    types = models.TextField()
    how_much_study = models.IntegerField()
    description = models.TextField()

    class Meta:
        app_label = "vuzes"
        ordering = ("how_much_study",)
        verbose_name = "Speciality"
        verbose_name_plural = "Specialities"

    def __str__(self):
        return self.types


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="FIO")
    born_date = models.DateField(verbose_name="was_born")
    where_born = models.TextField(verbose_name='Location')
    course = models.IntegerField(verbose_name="which_course")
    vuz_name = models.ForeignKey(to=VuzName, verbose_name="VUZ", on_delete=models.PROTECT)
    spec = models.ForeignKey(to=Speciality, verbose_name="Speciality", on_delete=models.PROTECT)

    class Meta:
        app_label = "vuzes"
        ordering = ("-born_date", "course")
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name
