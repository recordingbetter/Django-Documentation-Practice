from django.db import models


class Player(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length = 40)
    players = models.ManyToManyField(Player, through = 'TradeInfo')

    def __str__(self):
        return self.name


class TradeInfo(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    club = models.ForeignKey(Club, on_delete = models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField(null = True, blank = True)
