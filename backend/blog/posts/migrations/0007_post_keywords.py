# Generated by Django 3.0.14 on 2023-07-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20230713_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
