from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Pizza(models.Model):
    name = models.CharField(max_length = 30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        # 자신이 가지고있는 토핑목록을  함께 출력
        return '{} ({})'.format(self.name, ', '.join([p.name for p in self.toppings.all()]))

    class Meta:
        ordering = ('name',)
