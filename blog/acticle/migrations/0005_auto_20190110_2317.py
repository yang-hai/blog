# Generated by Django 2.1.5 on 2019-01-10 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acticle', '0004_auto_20190110_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acticle',
            name='c',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acticle.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='f',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acticle.Category'),
        ),
    ]