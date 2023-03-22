from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    # path("", views.view_routes),
    path("", views.root),
    path("get-category/", views.get_category, name="category"),
    path("get-class/", views.get_drug_class, name="drug-class"),
    path("drugs/", views.drug, name="drugs"),
    path("drugs/<int:pk>", views.single_drug, name="single-drugs"),
    path("city/", views.city, name="city"),
    path("pharma/", views.phrama, name="pharmacy"),
    path("city/<int:pk>", views.city_info, name="city-detail"),

    path("users/", views.user_list, name="user-list"),
    path("users/<int:pk>", views.get_user, name="single-user"),

    path("drugs/<int:pk>/price", views.DrugPrice.as_view(), name="drug-price"),
    path("drugs/<int:pk>/description", views.DrugDesc.as_view(), name="drug-description"),

    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 


]

urlpatterns = format_suffix_patterns(urlpatterns)