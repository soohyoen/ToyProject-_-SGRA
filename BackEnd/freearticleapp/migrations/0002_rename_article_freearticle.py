# Generated by Django 3.2.6 on 2021-09-07 06:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commentapp', '0005_comment_freearticle'),
        ('freearticleapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='FreeArticle',
        ),
    ]
