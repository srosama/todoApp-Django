from django.db import models

# Create your models here.
class ToDoInfo(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.title}"
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("main-list")
        