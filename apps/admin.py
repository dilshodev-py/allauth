import telebot
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Category, Ingredient


# Register your models here.
# bot = telebot.TeleBot("7845874862:AAGoP78o_YlrvHbVmXcKo6b2bxhSWsy8HVU")
#
#
# @admin.register(Product)
# class ProductModelAdmin(ModelAdmin):
#     def save_form(self, request, form, change):
#         data = form.cleaned_data
#         text = f"""
#             Product name : {data.get("name")}
#             Product price : {data.get("price")}
#         """
#         bot.send_message(-1002311783062 , text=text)
#         return super().save_form(request , form , change)



@admin.register(Category)
class ProductModelAdmin(ModelAdmin):
    pass

@admin.register(Ingredient)
class ProductModelAdmin(ModelAdmin):
    pass