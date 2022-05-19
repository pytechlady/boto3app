from rest_framework import serializers


class ProfileImageSerializer(serializers.Serializer):
    profile_image = serializers.ImageField()
    

class CoverImageSerializer(serializers.Serializer):
    cover_image = serializers.ImageField()