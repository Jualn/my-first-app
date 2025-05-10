from rest_framework.response import Response
from .models import Banners, Notices, Welcome
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from .serializer import BannerSerializer, NoticeSerializer, WelcomeSerializer


class BannerView(ReadOnlyModelViewSet):
    queryset = Banners.objects.filter(is_delete=False).order_by('-create_time')[:3]
    serializer_class = BannerSerializer

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        notice = Notices.objects.all().order_by('-create_time').first()
        notice_serializer = NoticeSerializer(instance=notice)
        return Response({"code": 100, "banners": res.data, "notice": notice_serializer.data})


class NoticeView(GenericViewSet, ListModelMixin):
    queryset = Notices.objects.all().order_by('-create_time')[:1]
    serializer_class = NoticeSerializer


class WelcomeView(GenericViewSet, RetrieveModelMixin):
    # /welcome/<pk>/    ->  对应ID
    queryset = Welcome.objects.all().order_by('-create_time')
    serializer_class = WelcomeSerializer
