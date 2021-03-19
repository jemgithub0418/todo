from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length= 256, blank = True)

class Batch(models.Model):
    batch = models.DateField(auto_now_add= True)

    class Meta:
        ordering = ['-batch']
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'

    def __str__(self):
        return self.batch.strftime("%B %d, %Y %A")


class Task(models.Model):
    title = models.CharField(
            max_length = 256,
            blank = False,
            null = False,
        )

    complete = models.BooleanField(
            default= False,
        )
    created = models.DateTimeField(auto_now_add= True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='author')

    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


