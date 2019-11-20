from django.shortcuts import render, get_object_or_404
from .serializers import TodoSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)

# user/1/
@api_view(['GET'])
def user_detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    # 요청이 들어온 JWT의 user 정보와 pk로 검색하여 나온 user객체의 정보가 같을 경우에만
    if request.user != user:
        return Response(status=404)
    serializer = UserSerializer(user)
    return Response(serializer.data)
