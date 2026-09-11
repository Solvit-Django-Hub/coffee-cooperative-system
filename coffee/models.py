from django.db import models


class CoffeeBatch(models.Model):
    GRADE_CHOICES = [('A', 'Grade A'), ('B', 'Grade B'), ('C', 'Grade C')]
    member = models.ForeignKey('members.Member', on_delete=models.CASCADE, related_name='batches')
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    harvest_date = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)