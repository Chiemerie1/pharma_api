from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    DrugCategories, DrugClasses, Drugs,
    City, Pharmacy
)
from .serializers import (
    DrugCategorySerializer, DrugClassesSerializer, DrugsSerializer,
    CitySerializer, PharmacySerializer
)




@api_view(["GET"])
def view_routes(request):
    routes = [
        {
            "endpoint": "/get-category/",
            "method": "GET and POST",
            "body": None,
            "description": "returns or adds to the list of the drug categories"
        },

        {
            "endpoint": "/get-class/",
            "method": "GET and POST",
            "body": None,
            "description": "returns or adds to the list of all drug classes"
        },

        {
            "endpoint": "/drugs/",
            "method": "GET and POST",
            "body": None,
            "description": "returns or adds to the list of all drugs"
        },

        {
            "endpoint": "/city/",
            "method": "GET and POST",
            "body": None,
            "description": "returns or adds to the list of all city"
        },

        {
            "endpoint": "/pharma/",
            "method": "GET and POST",
            "body": None,
            "description": "returns or adds to the list of all pharmacies"
        },
        
    ]
    return Response(routes)



@api_view(["GET", "POST"])
def get_category(request):

    if request.method == "GET":
        drug_category = DrugCategories.objects.all()
        serializer = DrugCategorySerializer(drug_category, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = DrugCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(["GET", "POST"])
def get_drug_class(request):
    
    if request.method == "GET":
        drug_class = DrugClasses.objects.all()
        serializer = DrugClassesSerializer(drug_class, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = DrugClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


@api_view(["GET", "POST"])
def drug(request):
    if request.method == "GET":
        drugs = Drugs.objects.all()
        serializer = DrugsSerializer(drugs, many=True)
        return Response(serializer.data)
    
    elif request.method =="POST":
        serializer = DrugsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(["GET", "POST"])
def city(request):

    if request.method == "GET":
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(["GET", "POST"])
def phrama(request):

    if request.method == "GET":
        pharmacy = Pharmacy.objects.all()
        serializer = PharmacySerializer(pharmacy, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = PharmacySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)