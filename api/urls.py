from django.urls import path
from . import views




urlpatterns = [
    path("", views.view_routes),
    path("get-category/", views.get_category),
    path("get-class/", views.get_drug_class),
    path("drugs/", views.drug),
    path("city/", views.city),
    path("pharma/", views.phrama),

]