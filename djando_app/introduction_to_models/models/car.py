from django.db import models


class ManuFacturer(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length = 40)
    manufacturer = models.ForeignKey(ManuFacturer, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
