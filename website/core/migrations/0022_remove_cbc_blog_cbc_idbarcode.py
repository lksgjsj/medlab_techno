# Generated by Django 4.2 on 2024-10-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_cbc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cbc',
            name='blog',
        ),
        migrations.AddField(
            model_name='cbc',
            name='idBarcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
