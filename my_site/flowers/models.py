from django.db import models

# Create your models here.
class Flowers(models.Model):
    name_flower = models.CharField(max_length=50)


    def __str__(self) -> str:
        return f"Kwiaty: {self.name_flower}"


