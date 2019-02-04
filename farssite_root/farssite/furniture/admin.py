from django.contrib import admin

from farssite.furniture.models import Furniture


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
	list_display = ('title', 'uploaded')
	list_filter = ('uploaded',)
