from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class dayoff(models.Model):
    type_choice = (
        ('0', 'ลากิจ'),
        ('1', 'ลาป่วย')
    )

    approve_status_choices = (
        ('0', 'ไม่อนุมัติ'),
        ('1', 'อนุมัติ'),
        ('3', 'รออนุมัติ')
    )

    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    type = models.CharField(max_length=1, choices=type_choice, default='3')
    date_start = models.DateField()
    date_end = models.DateField()
    approve_status = models.CharField(max_length=1, choices=approve_status_choices)

    def __str__(self):
        return f'{self.reason}'



