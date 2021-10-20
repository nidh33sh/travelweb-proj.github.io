from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class place1(models.Model):

    month = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to='picture')
    caption = models.TextField()
    desc1 = models.TextField()


    # id=int
    # name=str
    # image=str
    # descp=str
    # price=int
