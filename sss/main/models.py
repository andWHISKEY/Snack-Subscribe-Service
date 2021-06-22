from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Snack(models.Model):
    name=models.CharField(max_length=50, null=False)
    describe=models.CharField(max_length=500)
    summary =models.CharField(max_length=300)

    # image=models.ImageField(upload_to='images/', null=True)
    image=models.CharField(max_length=500)
    with_who =models.CharField(max_length=20)
    texture =models.CharField(max_length=20)
    flavor =models.CharField(max_length=20)
    is_one_time=models.CharField(max_length=20)
    situation =models.CharField(max_length=20)