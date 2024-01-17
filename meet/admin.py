from django.contrib import admin
from meet import models


admin.site.register(models.Reservation)
admin.site.register(models.WorkPlan)
admin.site.register(models.WorkingDay)
