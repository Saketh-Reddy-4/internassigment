from django.db import models

# Create your models here.
class Advisior(models.Model):
    name=models.CharField(max_length=10)
    photoUrl=models.CharField(max_length=2000)
    adv_id=models.IntegerField()

    def __str__(self):
        return self.name
