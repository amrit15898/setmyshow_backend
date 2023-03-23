from rest_framework import serializers
from .models import *

class EvenetSerilizer(serializers.ModelSerializer):
    class Meta:
        model = EventPost
        fields = "__all__"

 