from rest_framework import serializers
from .models import Banners, Notices,Welcome


class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welcome
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = '__all__'