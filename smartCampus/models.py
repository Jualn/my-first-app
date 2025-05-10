from django.contrib.auth.models import UserManager
from django.db import models


##### 创建用户表

class User(models.Model):
    objects = UserManager()
    avatar = models.ImageField(verbose_name='头像', upload_to="avatar/", default='welcome/OIP-C.jpg')
    username = models.CharField(verbose_name='用户名', max_length=10)
    age = models.IntegerField(verbose_name='年龄')
    gender = models.SmallIntegerField(verbose_name='性别', choices=((1, '男'), (2, '女'), (0, '保密')))
    introduction = models.TextField(verbose_name='简介', max_length=100)
    wechat_openid = models.CharField(verbose_name='openId', max_length=100)
    phone = models.CharField(verbose_name='手机号', max_length=11)

    class Meta:
        verbose_name_plural = "用户"


####### 创建欢迎表######
class Welcome(models.Model):
    objects = UserManager()
    img = models.ImageField(verbose_name='图片', upload_to='welcome/', default='welcome/on.jpg')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)


    class Meta:
        verbose_name_plural = "欢迎页"


#### 创建轮播图表模型#####
class Banners(models.Model):
    objects = UserManager()
    img = models.ImageField(upload_to="banners/", default='banners/一秒上瘾的小众英文歌_109951165055862669.jpg')
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        return str(self.img)

    class Meta:
        verbose_name_plural = "轮播图"


##### 通知表
class Notices(models.Model):
    objects = UserManager()
    content = models.CharField(verbose_name='内容',max_length=200, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    is_delete = models.BooleanField(verbose_name='是否删除',default=False)

    class Meta:
        verbose_name_plural = "通知"


##### 评论表
class Comments(models.Model):
    objects = UserManager()
    comment_avatar = models.OneToOneField(verbose_name='头像', to=User, related_name='comment_avatar',
                                          on_delete=models.CASCADE)
    commenter = models.ForeignKey(verbose_name='评论者', to=User, related_name='commenter', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='内容', max_length=200)
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = "评论"


##### blog表
class Post(models.Model):
    objects = UserManager()
    poster = models.ForeignKey(verbose_name='发布者', to=User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='内容', null=True, blank=True)
    views = models.IntegerField(verbose_name='浏览', default=0)
    likes = models.IntegerField(verbose_name='喜欢', default=0)
    comments = models.ForeignKey(verbose_name='评论', to=Comments, on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

    class Meta:
        verbose_name_plural = "博文"
