from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
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
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        print(request.user)
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
        print(request.user)
        objs = User.objects.all()
        serializer = UserSerializer(objs,many=True)
        return Response({
            "data": serializer.data
        })

    def patch(self, request):
        try:
            obj = User.objects.get(id=request.data['id'])

        except Exception as e:
            return Response({
                "message": "something went wrong"
            })  
        data = request.data
        serializer = UserSerializer(obj, data = data,partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "data successfully updated"

            })
        return Response({
            "message": "something went wrong"

        })


class GetSingleUser(APIView):
    def get(self, request, id):
        try:
            obj = User.objects.get(id=id)
        except Exception as e:
            return Response({
                "message": "something went wrong"
            })
        seriailzer = UserSerializer(obj)
        print(request.data)
        return Response({
            "data": seriailzer.data
            
        })
    def patch(self, request,id):
        try:
            obj = User.objects.get(id=id)
            print(obj)
        except Exception as e:
            return Response({
                "message": "invalid id"
            })
        data = request.data
        serializer = UserSerializer(obj, data = data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "message": "data updated successfully"
        })
        return Response({
            "message": "somethign went wrong"
        })

    def delete(self, request, id):
        try:
            obj = User.objects.get(id=id)
            obj.delete()
            return Response({
                "message": "deleted data successfully"
            })
        except Exception as e:
            pass
        return Response({
            "message": "something went wrong"
        })

    
