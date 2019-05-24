from django.db import models


class News(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=400)
    content = models.TextField()
