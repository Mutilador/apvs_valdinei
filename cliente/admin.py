from django.contrib import admin
from .models import Cliente, FipeDetail

# Register your models here.

class FipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo','ano','valor')

admin.site.register(Cliente)
admin.site.register(FipeDetail, FipeAdmin)