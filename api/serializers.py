from rest_framework import serializers
from django.contrib.auth.models import User
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
    owner = serializers.ReadOnlyField(source="owner.username")
    category = DrugCategorySerializer(read_only=True)
    drug_class = DrugClassesSerializer(read_only=True)
    category_id = serializers.IntegerField()
    drug_class_id = serializers.IntegerField()
    owner_id = serializers.IntegerField()



    class Meta:
        model = Drugs
        fields = "__all__"




class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["city", "code", "id"]


class PharmacySerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Pharmacy
        fields = ["name", "city"]



class UserSerializer(serializers.ModelSerializer):
    drugs = serializers.SlugRelatedField(many=True, queryset=Drugs.objects.all(), slug_field="name")
    # drugs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "drugs"]