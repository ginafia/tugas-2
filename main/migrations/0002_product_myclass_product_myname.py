# Generated by Django 4.2.5 on 2023-09-13 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='myclass',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='myname',
            field=models.CharField(default='', max_length=255),
        ),
    ]
