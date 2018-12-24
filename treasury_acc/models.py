from django.db import models

# Create your models here.
class treasury_acc(models.Model):
    id = models.AutoField(primary_key=True)
    rent_of_month = models.PositiveIntegerField()
    rent_of_year = models.PositiveIntegerField()
    rent_amt = models.DecimalField(max_digits=10,decimal_places=2)
    rent_paid_date = models.DateField()
    tenant_id = models.ForeignKey('tenant.tenant',related_name='tenant_id+',null=True,on_delete= models.CASCADE)
