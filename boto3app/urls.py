from django.urls import path
from .views import *


urlpatterns = [
    path('profile', UploadProfileImage.as_view(), name='profile'),
]