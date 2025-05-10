from django.urls import path

from .views import BannerView,NoticeView ,WelcomeView  #没有导入总的views的话就需要单个导入视图函数
#from smartCampus import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('banners',BannerView,'banners')
router.register('notice',NoticeView,'notice')
router.register('welcome',WelcomeView,'welcome')
urlpatterns = [
    # path('welcome/', welcome),
]
urlpatterns += router.urls