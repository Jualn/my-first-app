# Generated by Django 5.1.7 on 2025-04-25 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartCampus', '0012_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banners',
            options={'verbose_name_plural': '轮播图'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='notices',
            options={'verbose_name_plural': '通知'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': '博文'},
        ),
        migrations.AlterModelOptions(
            name='welcome',
            options={'verbose_name_plural': '欢迎页'},
        ),
    ]
