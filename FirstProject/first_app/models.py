from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.contact_number}'