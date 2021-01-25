# views.py
from rest_framework import viewsets

from .serializers import OsobaSerializer
from .models import Osoba


class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all().order_by('name')
    serializer_class = OsobaSerializer