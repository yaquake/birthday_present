from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Painting(models.Model):
    author = models.CharField(max_length=50)
    link = models.CharField(max_length=200, default='http://facebook.com')
    image = models.ImageField(upload_to='paintings/')

    def __str__(self):
        return self.author


@receiver(post_delete, sender=Painting)
def delete_image(sender, instance, **kwargs):
    instance.image.delete(False)