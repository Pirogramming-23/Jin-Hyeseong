from django.db import models

# Create your models here.

class DevTool(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.name