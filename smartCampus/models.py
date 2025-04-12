from django.db import models


# Create your models here.

### 创建广告页面表模型###

class Welcome(models.Model):
    # upload_to 图片上传后，放到 media文件夹下的welcome文件夹下
    # ImageField接受的图片类型，最终会存到media文件夹下"welcome/"这个路径的文件夹
    # 如果图片没上传，有个默认图片地址default='welcome/default.jpg'
    # 要使用这个ImageField上传文件需要安装pillow这个模块           pip3 install pillow
    # 如果使用CharField--》图片需要自己保存，然后把地址放在CharField这个字段上
    img = models.ImageField(upload_to="welcome/", default='welcome/OIP-C.jpg')
    # IntegerField：整数字段类型
    order = models.IntegerField(default=0)
    # 这个字段以后不用传，会自动把图片上传的时间存到数据库
    create_time = models.DateTimeField(auto_now=True)
    # 前端删除不显示
    is_delete = models.BooleanField(default=False)

    class Meta:
        # 在admin中，表是中文
        verbose_name_plural = '欢迎表'


#### 创建轮播图表模型#####
class Banners(models.Model):
    img = models.ImageField(upload_to="banners/", default='banners/一秒上瘾的小众英文歌_109951165055862669.jpg')
    order = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    def __str__(self):
        return str(self.img)