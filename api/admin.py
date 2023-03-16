from django.contrib import admin
from .models import (
    DrugCategories, DrugClasses, Drugs,
    City, Pharmacy
)

# Register your models here.

admin.site.register(DrugCategories)
admin.site.register(DrugClasses)
admin.site.register(Drugs)
admin.site.register(City)
admin.site.register(Pharmacy)