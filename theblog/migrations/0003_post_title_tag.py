# Generated by Django 3.2.5 on 2021-07-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My personal blog', max_length=225),
        ),
    ]
