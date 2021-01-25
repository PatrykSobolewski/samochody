# serializers.py
from rest_framework import serializers

from .models import Osoba
from .models import Samochod
from django.contrib.auth.models import User

class OsobaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Osoba
        fields = '__all__'

class SamochodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Samochod
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'age', 'model', 'marka']