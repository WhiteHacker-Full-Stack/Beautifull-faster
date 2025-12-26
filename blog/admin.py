from django.contrib import admin

# Register your models here.
from .models import Beauty, Products, Coment
admin.site.register(Beauty)

admin.site.register(Coment)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {"bosh": ('name','text','price')}
    ordering = ('name',)