from django.db import models

# Create your models here.

class Male(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)

class Text(models.Model):
    title = models.CharField(max_length=40, default="Title")
    text = models.TextField()

    def __str__(self):
        return self.title
