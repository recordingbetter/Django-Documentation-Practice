from datetime import date
from django.db.models import Q

from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length = 40)
    players = models.ManyToManyField(
        Player,
        through = 'TradeInfo',
        through_fields = ('club', 'player'),
        related_name = "%(app_label)s_%(class)s_related",
    )

    # current_club 프로퍼티에 현재 속하는 Club 리턴
    @property
    def current_club(self):
        return 'current club is {}'.format(self.name)

    def __str__(self):
        return self.name

        # squad 메서드에 현직 선수들만 리턴
        # 인수로 년도(2017, 2015...등)를 받아
        # 해당 년도의 현직 선수들을 리턴,
        # 주어지지 않으면 현재를 기준으로 함
    def squad(self, year = None):
        if year is None:
            year = timezone.now().year
        else:
            pass
        player_list = self.players.filter(
            Q(tradeinfo__date_joined__year__lte = year),
            (Q(tradeinfo__date_leaved__gte = date(year, 12, 31)) |
             Q(tradeinfo__date_leaved__isnull = True))
        )
        return print(', '.join([p.name for p in player_list]))


class TradeInfo(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    club = models.ForeignKey(Club, on_delete = models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField(null = True, blank = True)
    # 2. recommender 와 prev_club(이전 클럽)을 활성화시키고 Club 의 MTM 필드에 through_fields 를 명시
    recommender = models.ForeignKey(
        Player,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name = 'trade_recommender',
    )
    prev_club = models.ForeignKey(
        Club,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name = 'trade_prev_club')

    def __str__(self):
        return 'Player {} is joined club {} at {}.\nAnd left the club at {}'.format(
            self.player,
            self.club,
            self.date_joined,
            self.date_leaved,
        )

    # current_tradeinfo 프로퍼티에 현재 자신의 TradeInfo 리턴
    @property
    def current_tradeinfo(self):
        if self.date_leaved:
            return print('Player {} is joined club {} at {}.\nAnd left the club at {}'.format(
                self.player,
                self.club,
                self.date_joined,
                self.date_leaved,
            ))
        else:
            return print('Player {} is joined club {} at {}.\nAnd never left.'.format(
                self.player,
                self.club,
                self.date_joined,
            ))
            # prev_club = 이전 Club

    # 1. property 로 is_current 속성이 TradeInfo 가 현재 현직(leaved 하지 않았는지)여부 반환
    @property
    def is_current(self):
        if self.date_leaved:
            return print('Player {} is joined club {} at {}.\nAnd left the club at {}'.format(
                self.player,
                self.club,
                self.date_joined,
                self.date_leaved,
            ))
        else:
            return print('Player {} is joined club {} at {}.\nAnd never left.'.format(
                self.player,
                self.club,
                self.date_joined,
            ))
