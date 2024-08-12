
# diagnosis/models.py
from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.TextField()
    description = models.TextField()
    prevention = models.TextField()
    treatment = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name
