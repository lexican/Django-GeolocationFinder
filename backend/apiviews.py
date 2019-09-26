from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import General_details
from .serializers import General_detailsSerializer
from rest_framework import generics

import requests
from django.core.cache import cache

#API list view
class GeoList(generics.ListCreateAPIView):
    queryset = General_details.objects.all()
    serializer_class = General_detailsSerializer


class GeoDetail(APIView):
    def get(self, request, ip):
        detail = General_details.objects.filter(ip=ip)
        if detail:
            object = get_object_or_404(General_details, ip=ip)
            data = General_detailsSerializer(object).data
        else:
            #get the data from ipstack and save in a memcache
            cache_key = ip  # needs to be unique
            cache_time = 86400  # time in seconds for cache to be valid
            data = cache.get(cache_key)  # returns None if no key-value pair
            if not data:
                url = 'https://api.ipstack.com/'+ ip + '? access_key =' + 'YOUR_ACCESS_KEY'
                r = requests.get(url)
                data = r.json()
            cache.set(cache_key, data, cache_time)
        return Response(data)