from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
from .models import Welcome
from django.http import JsonResponse


# 广告接口比较low，使用fbv写的，后期一般不会这样写
def welcome(request):
    res = Welcome.objects.all().order_by('-order').first()
    img = 'http://127.0.0.1:8000/media/' + str(res.img)
    return JsonResponse({'code': 100, 'msg': '成功', 'result': img})


# 轮播图接口，使用drf写
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from .models import Banners
from .serializer import BannerSerializer


class BannerView(GenericViewSet, ListModelMixin):
    queryset = Banners.objects.filter(is_delete=False).order_by('order')[:3]
    serializer_class = BannerSerializer
