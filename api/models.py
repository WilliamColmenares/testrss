from django.db import models


class News(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=400)
    content = models.TextField()


class TrainBase(models.Model):
    name = models.CharField(max_length=120)
    class Meta:
        abstract = True


class Section(TrainBase):
    pass


class People(TrainBase):
    lastname = models.CharField(max_length=120)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)


class ICE(TrainBase):
    sections = models.ManyToManyField(Section)
