from django.contrib import admin
from .models import CarMake, CarModel
# from .models import related models


class CarModelAdmin(admin.ModelAdmin):
    list_display= ("make", "name","year")
# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel,CarModelAdmin)

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
