import datetime
from django.db import models

# Create your models here.

position_type = (
    ("TEAMLEAD", "Teamlead"),
    ("SENIOR", "Senior"),
    ("MIDDLE", "Middle"),
    ("JUNIOR", "Junior"),
    ("INTERN", "Intern")
)


class Employee(models.Model):
    first_name = models.CharField("First name", null=True, blank=True, max_length=20)
    last_name = models.CharField("Last name", null=True, blank=True, max_length=20)
    position = models.CharField("Position", choices=position_type, max_length=20)
    joined_at = models.DateField("Joined at", null=True, blank=True, default=datetime.date.today())
    salary = models.PositiveIntegerField("Salary", null=True, blank=True)
    parent_id = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return '%s, %s,  %s' % (self.id, self.first_name, self.last_name)
