from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
# Create your views here.
def artist_login(request):
    if request.method == "POST":
        artist_band_type = request.POST.get("artist_type")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        user = User(artist_type_band = artist_band_type, username = name, email = email, contact=phone)
        user.set_password(password)
        user.save()

    return render(request, "accounts/artist_login.html")

class SignupApi(APIView):
    def post(self, request):
        data = request.data 
        print(data)
        serializer = UserSerializer(data = data )
        if serializer.is_valid():
            print("hello")
            serializer.save()
            return Response({
                "message": "data successfully posted"
            })
        return Response({
            'message': 'something went wrong'
        })

    def get(self, request):
        objs = User.objects.all()
        serializer = UserSerializer(objs,many=True)
        return Response({
            "data": serializer.data
        })

