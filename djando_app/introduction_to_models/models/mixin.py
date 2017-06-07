from django.db import models
from utils.models.mixin import TimeStampedMixin


# TimeStampedMixin (추상클래스)를 만들어 반복되는 필드들을 상속받는다.
# models.Model 은 TimeStampedMixin 에서 이미 상속받았으므로 필요없다.
class User(TimeStampedMixin):
    name = models.CharField(max_length = 30)


class Post(TimeStampedMixin):
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    title = models.CharField(max_length = 100)
    content = models.TextField()


class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    content = models.TextField()
