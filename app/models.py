from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class H1BData(models.Model):
    __tablename__ = 'h1b_data'
    case_number = models.CharField(max_length=32, primary_key=True)
    wage_rate_of_pay = models.FloatField(null=False,validators=[MinValueValidator(0.0)])
    wage_unit_of_pay = models.FloatField(null=False,validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.case_number