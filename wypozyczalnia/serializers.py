# serializers.py
from rest_framework import serializers

from .models import Osoba

class OsobaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Osoba
        fields = ('name', 'surname')