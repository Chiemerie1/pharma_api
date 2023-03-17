from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path("", views.view_routes),
    path("get-category/", views.get_category),
    path("get-class/", views.get_drug_class),
    path("drugs/", views.drug),
    path("city/", views.city),
    path("pharma/", views.phrama),
    path("city/<int:pk>", views.city_info),

    path("users/", views.user_list),
    path("users/<int:pk>", views.get_user)

]

urlpatterns = format_suffix_patterns(urlpatterns)