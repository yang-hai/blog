# Generated by Django 2.1.5 on 2019-01-10 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acticle', '0003_auto_20190110_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acticle',
            old_name='c_id',
            new_name='c',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='f_id',
            new_name='f',
        ),
    ]
