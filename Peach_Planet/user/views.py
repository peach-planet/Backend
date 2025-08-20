from django.shortcuts import render
from .models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import *
from django.contrib.auth import login

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # 회원가입 성공 시 자동 로그인
        login(request, user)
        # 토큰 생성
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'message': '회원가입이 완료되었습니다.',
            'user': {
                'id': user.user_id,
                'nickname': user.nickname
            },
            'token': token.key
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        login(request, user)
        # 토큰 생성
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'message': '로그인이 완료되었습니다.',
            'user': {
                'id': user.user_id,
                'nickname': user.nickname
            },
            'token': token.key
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
