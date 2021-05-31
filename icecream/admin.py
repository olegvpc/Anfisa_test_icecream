from django.contrib import admin

from .models import Icecream, Friend


class IcecreamAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


class FriendAdmin(admin.ModelAdmin):
    list_display = ("friend_name", "friend_city", "friend_icecream")


admin.site.register(Icecream, IcecreamAdmin)
admin.site.register(Friend, FriendAdmin)