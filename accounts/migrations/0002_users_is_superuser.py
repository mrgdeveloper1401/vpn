# Generated by Django 4.2.6 on 2023-10-05 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='superuser status'),
        ),
    ]
