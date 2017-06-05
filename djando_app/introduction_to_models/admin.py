from django.contrib import admin

# Register your models here.
from .models.person import Person
from .models.intermediate import Player, Club, TradeInfo


admin.site.register(Person)
admin.site.register(Player)
admin.site.register(Club)
admin.site.register(TradeInfo)

