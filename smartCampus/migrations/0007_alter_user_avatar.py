# Generated by Django 5.1.7 on 2025-04-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartCampus', '0006_alter_comments_comment_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='welcome/OIP-C.jpg', upload_to='avatar/', verbose_name='头像'),
        ),
    ]
