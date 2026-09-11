from django.db import models
from django.conf import settings

class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='member_profile')
    membership_number = models.CharField(max_length=20, unique=True, editable=False)
    farm_location = models.CharField(max_length=255)
    national_id = models.CharField(max_length=20, unique=True)
    date_joined = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.membership_number:
            last = Member.objects.order_by('-id').first()
            next_id = (last.id + 1) if last else 1
            self.membership_number = f"MEM-{next_id:06d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.membership_number