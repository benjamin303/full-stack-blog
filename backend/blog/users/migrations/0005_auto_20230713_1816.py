# Generated by Django 3.0.14 on 2023-07-13 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
