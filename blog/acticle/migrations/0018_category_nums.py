# Generated by Django 2.1.5 on 2019-01-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acticle', '0017_auto_20190112_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='nums',
            field=models.IntegerField(default=0),
        ),
    ]
