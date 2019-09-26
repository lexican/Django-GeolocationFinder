from django.urls import path

from .views import index, geoLocation

urlpatterns = [
    path("", index, name="index"),
    path("<str:ip>/", geoLocation, name="geo_detail")
]