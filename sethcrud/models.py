from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=45, blank=False, null=False)
    email = models.CharField(max_length=60, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    gender = models.CharField(max_length=6, blank=False, null=False)
    contact = models.IntegerField(blank=False, null=False)
    amount = models.IntegerField(blank=False, null=False)


    def __str__(self):
        return self.name
