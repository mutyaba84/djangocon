from django.shortcuts import render

from .models import Variable
from .serializers import VariableSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class VariableViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer
