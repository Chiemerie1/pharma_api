from rest_framework import serializers
from .models import (
    DrugCategories, DrugClasses, Drugs,
    City, Pharmacy
)



class DrugCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugCategories
        fields = ["cat_name"]


class DrugClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugClasses
        fields = ["class_name"]

        

class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["city", "code"]


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ["name", "city"]