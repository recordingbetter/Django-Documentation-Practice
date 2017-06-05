from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    # current_club프로퍼티에 현재 속하는 Club리턴
    # current_tradeinfo프로퍼티에 현재 자신의 TradeInfo리턴


class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,
        through='TradeInfo',
    )

    def __str__(self):
        return self.name

    def squad(self, year=None):
        pass
        # squad메서드에 현직 선수들만 리턴
        # 인수로 년도(2017, 2015...등)를 받아
        # 해당 년도의 현직 선수들을 리턴,
        # 주어지지 않으면 현재를 기준으로 함


class TradeInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField(null=True, blank=True)
    # recommender = models.ForeignKey(Player, on_delete=models.CASCADE)
    # prev_club = 이전 Club

    # 1. property로 is_current 속성이 TradeInfo가 현재 현직(leaved하지 않았는지)여부 반환
    # 2. recommender와 prev_club을 활성화시키고 Club의 MTM필드에 through_fields를 명시


# 위의 요구조건들을 만족하는 실행코드 작성