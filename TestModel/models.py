from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

# class employees(models.Model):
#     employee_id = models.IntegerField(primary_key=True)
#     first_name = models.CharField(max_length=20, null=True)
#     last_name = models.CharField(max_length=25)
#     email = models.CharField(max_length=25)
#
#     class Meta:
#         db_table = "employees"
#

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    st = models.BooleanField(default=False, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'test'
