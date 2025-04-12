from django.urls import path

from .views import welcome, BannerView  # 没有导入总的views的话就需要单个导入视图函数
#from smartCampus import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('banners',BannerView,'banners')
urlpatterns = [
    path('welcome/', welcome),

]
urlpatterns += router.urls