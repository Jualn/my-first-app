from django.contrib import admin

# Register your models here.

from .models import Banners,Notices,User,Comments,Post,Welcome

class WelcomeManage(admin.ModelAdmin):
    list_display = ['img','create_time','is_delete']

class BannersManage(admin.ModelAdmin):
    list_display = ('img','create_time','is_delete')

class NoticesManage(admin.ModelAdmin):
    list_display = ('content','create_time','is_delete')

class CommentsManage(admin.ModelAdmin):
    list_display = ('comment_avatar','commenter','content','create_time')

class UserManage(admin.ModelAdmin):
    list_display = ('avatar','username')

class PostManage(admin.ModelAdmin):
    list_display = ('poster','text','views','likes','comments','create_time')

admin.site.register(Welcome,WelcomeManage)
admin.site.register(Banners,BannersManage)
admin.site.register(Notices,NoticesManage)
admin.site.register(Comments,CommentsManage)
admin.site.register(User,UserManage)
admin.site.register(Post,PostManage)


