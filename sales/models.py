from django.db import models


class Sale(models.Model):
    batch = models.ForeignKey('coffee.CoffeeBatch', on_delete=models.PROTECT, related_name='sales')
    buyer_name = models.CharField(max_length=255)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField()