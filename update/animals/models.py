from django.db import models

class Animals(models.Model):
    species = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    photo = models.URLField()

    class Meta:
        db_table = 'all_animals'
        ordering = ['id']

    def __str__(self):
        return f"{self.species} - {self.sex} - {self.age}"