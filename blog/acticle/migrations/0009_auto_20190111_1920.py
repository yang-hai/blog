# Generated by Django 2.1.5 on 2019-01-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acticle', '0008_category_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.TextField(default='无', max_length=400),
        ),
        migrations.AlterField(
            model_name='category',
            name='keywords',
            field=models.CharField(default='无', max_length=20),
        ),
    ]
