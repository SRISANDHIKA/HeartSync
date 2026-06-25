from django.db import models
from doctors.models import Doctor

# Create your models here.
class Patient(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  gender = models.CharField(max_length=10)
  phone = models.CharField(max_length=15)

  doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        null=True,
        blank=True
)
  def __str__(self):
    return self.name