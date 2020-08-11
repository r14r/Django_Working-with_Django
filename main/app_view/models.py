from django.db import models

class DataItem(models.Model):
    text = models.CharField(max_length=200)
    data = models.IntegerField(default=0)

    def __str__(self):
        return self.text