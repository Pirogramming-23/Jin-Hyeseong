from django.db import models
from apps.devtools.models import DevTool

# Create your models here.

class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="idea_thumbnails/", blank=True, null=True)
    content = models.TextField()
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, related_name="ideas")
    interest = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_star = models.BooleanField(default=False)

    def __str__(self):
        return self.title

