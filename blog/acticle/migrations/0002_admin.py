# Generated by Django 2.1.5 on 2019-01-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acticle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
    ]
