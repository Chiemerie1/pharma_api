from rest_framework import status, renderers
from rest_framework.decorators import api_view, permission_classes, renderer_classes, authentication_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BaseAuthentication

from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import GenericAPIView

from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView

from .models import (
    DrugCategories, DrugClasses, Drugs,
    City, Pharmacy
)

from .serializers import (
    DrugCategorySerializer, DrugClassesSerializer, DrugsSerializer,
    CitySerializer, PharmacySerializer, UserSerializer
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
        {
            
            "description": "You can search for individual items by adding the primary key after a slash"
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
            



# @permission_classes((IsOwnerOrReadOnly, IsAuthenticated))
@api_view(["GET", "POST"])
@cache_page(60*60*2)
@vary_on_cookie
def drug(request, format=None):
    drugs = Drugs.objects.all()
    serializer = DrugsSerializer(drugs, many=True)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes((IsOwnerOrReadOnly, IsAuthenticated))
def single_drug(request, pk):
    try:
        drug = Drugs.objects.get(pk=pk)
    except drug.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serialiizer = DrugsSerializer(drug)
        return Response(serialiizer.data)
    
    elif request.method == "PUT":
        serialiizer = DrugsSerializer(drug, data=serialiizer.data)
        if serialiizer.is_valid():
            serialiizer.save()
        return Response(serialiizer.data, status=status.HTTP_200_OK)
    
    elif request.method == "DELETE":
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif drug is None:
        return Response(serialiizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        


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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(["GET", "POST"])
def city(request, format=None):

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
    



@api_view(["GET", "PUT", "DELETE"])
def city_info(request, pk):

    """
        This function gets, modifies, and deletes a city.
    """
    try:
        city = City.objects.get(pk=pk)
    except city.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CitySerializer(city)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# serializing the user
@api_view(["GET"])
def user_list(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)
    


@api_view(["GET"])
def get_user(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user)
    return Response(serializer.data)


# Creating endpoint for the root of the API
@api_view(["GET"])
def root(request, format=None):
    return Response({
        "users": reverse(user_list, request=request, format=format),
        "drugs": reverse(drug, request=request, format=format),
        "drug_class": reverse(get_drug_class, request=request, format=format),
        "pharmacy": reverse(phrama, request=request, format=format),
        "city": reverse(city, request=request, format=format),
        "category": reverse(get_category, request=request, format=format),
    })




class DrugPrice(GenericAPIView):
    queryset = Drugs.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        drug = self.get_object()
        return Response(drug.price)
    


class DrugDesc(GenericAPIView):
    queryset = Drugs.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        drug = self.get_object()
        return Response(drug.description)
    


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer