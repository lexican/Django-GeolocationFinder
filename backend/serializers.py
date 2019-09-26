from rest_framework import serializers
from .models import General_details


class General_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = General_details
        fields = '__all__'