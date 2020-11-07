from django.db import models


class Student(models.Model):
    roll_no = models.CharField(max_length=8)
    name = models.CharField(max_length=32)
    father_name = models.CharField(max_length=32)
    email_id = models.CharField(max_length=32)
    phone_no = models.CharField(max_length=15)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no

