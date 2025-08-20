from django.urls import path, include
from rest_framework import routers

from .views import *

app_name="blog"

router_post = routers.DefaultRouter()
router_post.register('', BlogViewSet)

urlpatterns = [
    path('', include(router_post.urls)),
  
]