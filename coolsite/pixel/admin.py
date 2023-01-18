from django.contrib import admin

from .models import *


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'best', 'janr') # что мы видим
    list_display_links = ('id', 'title') # что мы можем выбрать
    search_fields = ('title', 'content') # что мы можем найти
    list_editable = ('content',) # список редактируемых полей


class BestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'photo', 'time_create')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('content',)

class JanrAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'time_create')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('content',)

admin.site.register(Game, GameAdmin)
admin.site.register(Best, BestAdmin)
admin.site.register(Janr, JanrAdmin)