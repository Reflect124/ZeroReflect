from django.db import models
from django.utils import timezone


# Create your models here.

class Carousel(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    shortText = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='Carousel')

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100)
    firstImpression = models.CharField(max_length= 250, default="We Are success")
    description = models.TextField()
    image = models.ImageField(upload_to='About')
    ourMission = models.CharField(max_length=500, default="Our Mission")
    ourVision = models.CharField(max_length=500,default='Our Vision')

    def __str__(self):
        return self.title

    def textFild(self):
        return self.description[:300] + '... ... ...'

class Bolg(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Blog')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def textBolg(self):
        return self.description[:200] + '... ...'

    class Meta:
        ordering = ['-modified']

class Service(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='Service')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    website = models.URLField(max_length=600, blank=True)

    def __str__(self):
        return self.title


class ClientProfile(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='Client')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    website = models.URLField(max_length=600, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modified']


class Footer(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='Footer')
    website = models.URLField(max_length=600, blank=True)

    def __str__(self):
        return self.title
