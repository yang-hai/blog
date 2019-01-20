from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=150, null=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'




