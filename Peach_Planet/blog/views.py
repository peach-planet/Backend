from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import Blog
from .serializers import *

from rest_framework.permissions import IsAuthenticated

#Viewset

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # 로그인한 사용자를 writer로 자동 저장
        serializer.save(writer=self.request.user)

   