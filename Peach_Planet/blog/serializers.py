from rest_framework.serializers import ModelSerializer
from .models import Blog

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__' # 모든 필드를 직렬화
        #fields = ['id', 'writer', 'content'] # 특정 필드만 직렬화
        

