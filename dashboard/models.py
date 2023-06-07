from django.db import models

# Create your models here.
class CountryData(models.Model):
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    # string representation of the model
    def __str__(self):
        return f'{self.country} - {self.population}'
    
    class Meta:
        verbose_name_plural = 'Country Population Data'

