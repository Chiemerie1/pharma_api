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
    category = DrugCategorySerializer()
    drug_class = DrugClassesSerializer()

    class Meta:
        model = Drugs
        fields = "__all__"

    def create(self, validated_data):
        name = validated_data.get("name")
        category = validated_data.pop("category")
        drug_class = validated_data.pop("drug_class")
        description = validated_data.get("description")
        availability = validated_data.get("availability")
        owner = validated_data.get("owner.username")

        owner = User.objects.all().filter(username=owner)

        drug = Drugs.objects.create( **validated_data)

        for cat in category:
            DrugCategories.objects.create(drug=drug, **category)

        for clas in drug_class:
            DrugClasses.objects.create(drug=drug, **drug_class)
            

        return drug




class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["city", "code"]


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ["name", "city"]



class UserSerializer(serializers.ModelSerializer):
    # drugs = serializers.SlugRelatedField(many=True, queryset=Drugs.objects.all(), slug_field="name")
    drugs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "drugs"]