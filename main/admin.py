from django.contrib import admin
from main.models import Zombie, Tweet

class ZombieAdmin(admin.ModelAdmin):
	list_display = ('name', 'cemetery',)
	search_field = ('name',)

class TweetAdmin(admin.ModelAdmin):
	list_display = ('status','zombie','created_at',)


admin.site.register(Zombie, ZombieAdmin)
admin.site.register(Tweet, TweetAdmin)
