from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','size','order_status','quantity','created_at']
    list_filter = ['created_at','order_status','size']