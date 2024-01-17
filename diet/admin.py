from django.contrib import admin
from diet import models

admin.site.register(models.Meal)
admin.site.register(models.Dishes)
admin.site.register(models.Diet)

