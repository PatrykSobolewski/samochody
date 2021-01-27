# views.py
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import OsobaSerializer, SamochodSerializer
from .models import Osoba
from .models import Samochod
from  .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all().order_by('name')
    serializer_class = OsobaSerializer
    name = 'osobaa'

class SamochodViewSet(viewsets.ModelViewSet):
    queryset = Samochod.objects.all().order_by('model')
    serializer_class = SamochodSerializer
    name = 'models'

class OsobaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    name = 'osoba'
    permission_classes = [IsAuthenticated]


class SamochodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod'
    permission_classes = [IsAuthenticated]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users'
    permission_classes = [IsAuthenticated]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user'
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({'osoba': reverse(OsobaViewSet.name, request=request),
                         'samochod': reverse(SamochodViewSet.name, request=request),
                         'users': reverse(UserList.name, request=request)
                         })