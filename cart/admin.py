from django.contrib import admin
from . import models
# Register your models here.


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','is_paid']
    inlines = (OrderItemAdmin,)
    list_filter = ['is_paid']
    
    
    
