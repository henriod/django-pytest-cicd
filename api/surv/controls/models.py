from django.db import models
from django.utils.timezone import now

# Create your models here.
class Control(models.Model):
    class ControlTypes(models.TextChoices):
        Primary = "Primary"
        Secondary = "Secondary"
        Tertiary = "Tertiary"
    name = models.CharField(max_length=30, unique=True)
    cid = models.CharField(max_length=10, unique=True)
    ctype = models.CharField(choices=ControlTypes.choices, max_length=10)
    last_update =models.DateTimeField(default=now, editable=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
