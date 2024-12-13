from django.contrib import admin
from . import models
from jalali_date.admin import ModelAdminJalaliMixin
# Register your models here.

admin.site.site_title = "پنل مدیریت"
admin.site.site_header = "پنل مدیریت تکنو لند"
@admin.register(models.Product)
class ProductAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ["title","price","updated","quantity"]

@admin.register(models.TeamMember) 
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ["name","job"]
    
@admin.register(models.CommentProduct)
class CommentProductAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ["product","author","created"]


   
admin.site.register(models.Color)
admin.site.register(models.Category)
admin.site.register(models.Contact)