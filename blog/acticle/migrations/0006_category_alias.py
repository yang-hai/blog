# Generated by Django 2.1.5 on 2019-01-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acticle', '0005_auto_20190110_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='alias',
            field=models.CharField(max_length=50, null=True),
        ),
    ]