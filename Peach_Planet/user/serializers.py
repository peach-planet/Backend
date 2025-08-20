from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = CustomUser
        fields = ['user_id', 'nickname', 'password']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            user_id=validated_data['user_id'],
            nickname=validated_data['nickname'],
            password=validated_data['password'],
        )
        return user

class LoginSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        user_id = attrs.get('user_id')
        password = attrs.get('password')
        
        if user_id and password:
            user = authenticate(user_id=user_id, password=password)
            if not user:
                raise serializers.ValidationError('이메일 또는 비밀번호가 올바르지 않습니다.')
            if not user.is_active:
                raise serializers.ValidationError('비활성화된 계정입니다.')
            attrs['user'] = user
        else:
            raise serializers.ValidationError('아이디와 비밀번호를 모두 입력해주세요.')
        
        return attrs

