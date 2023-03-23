from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class EventApi(ListAPIView, CreateAPIView):
    serializer_class = EvenetSerilizer
    queryset = EventPost.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['requirements']
    # def get_queryset(self):
    #     queryset1 = EventPost.objects.all()
    #     requirement = self.request.query_params.get('requirement', None)
    #     print(requirement)
    #     if requirement:
    #         queryset =  queryset1.filter(requirements = requirement)
            
    #         if queryset:
    #             return queryset
    #     queryset = queryset1

    #     return queryset
    
    