# Generated by Django 3.0.5 on 2022-03-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.IntegerField(default=1),
        ),
    ]
