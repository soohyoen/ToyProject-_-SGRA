# Generated by Django 3.2.6 on 2021-08-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='max_personnel',
            field=models.CharField(choices=[('상관없음', '상관없음'), ('1~2명', '1~2명'), ('3~4명', '3~4명'), ('5~6명', '5~6명'), ('6명이상', '6명이상')], default=True, max_length=10),
        ),
        migrations.AddField(
            model_name='article',
            name='progress_method',
            field=models.CharField(choices=[('전체', '전체'), ('어학', '어학'), ('취업', '취업'), ('고시/공무원', '고시/공무원'), ('취미/교양', '취미/교양'), ('프로그래밍', '프로그래밍'), ('기타', '기타')], default=True, max_length=10),
        ),
        migrations.AddField(
            model_name='article',
            name='region',
            field=models.CharField(choices=[('서울특별시', '서울특별시'), ('경기도', '경기도'), ('강원도', '강원도'), ('충청도', '충청도'), ('전라도', '전라도'), ('경상도', '경상도'), ('제주도', '제주도')], default=True, max_length=10),
        ),
    ]
