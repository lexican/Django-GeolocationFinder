from django.urls import path
from .apiviews import GeoList, GeoDetail

urlpatterns = [
    path("", GeoList.as_view(), name="geo_list"),
    path("<str:ip>/", GeoDetail.as_view(), name="geo_detail")
]