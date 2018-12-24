from django.db import models

# Create your models here.
class leaserenewal(models.Model):
    id = models.AutoField(primary_key=True)
    landlord_name = models.ForeignKey('managment.owner',related_name="owner_name+",null=True,on_delete=models.CASCADE)
    tenant_name = models.ForeignKey('tenant.tenant',related_name="tenant_name+",null=True,on_delete=models.CASCADE)
    PROPERTY = (
        ('apartment','APARTMENT'),
        ('flat','FLAT')
    )
    property = models.CharField(max_length=100,choices=PROPERTY,default='True')
    start_date = models.DateField()
    end_date = models.DateField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    STATES = (
        ('KARANATAKA', 'KARANATAKA'),
        ('DEHLI', 'DEHLI'),
        ('HARIYANA', 'HARIYANA'),
        ('KERALA', 'KERALA'),
        ('TAMILNADU', 'TAMILNADU'),
        ('ANDHRA PRADESH', 'ANDHRA PRADESH'),
        ('TELANGANA', 'TELANGANA'),
        ('BIHARA', 'BIHARA'),
        ('MADHYA PRADESH', 'MADHYA PRADESH'),
        ('PUNJAB', 'PUNJBA'),
        ('GOA', 'GOA'),
        ('J&K', 'J&K'),
        ('Assam', 'ASSAM'),
        ('Chhattisgarh', 'CHHATTISGARH'),
        ('GUJARAT', 'GUJARAT'),
        ('Himachal Pradesh', 'HIMACHAL PRADESH'),
        ('Haryana', 'HARYANA'),
        ('Jharkhand', 'JHARKHAND'),
        ('Maharashtra', 'MAHARASHTA'),
        ('Manipur', 'MANIPUR'),
        ('Meghalaya', 'MEGHALAYA'),
        ('Mizoram', 'MIZORAM'),
        ('Nagaland', 'NAGALAND'),
        ('Odisha', 'ODISHA'),

    )

    state = models.CharField(max_length=10, choices=STATES, default='True')
    pincode = models.IntegerField()

class renewal(models.Model):
    id = models.AutoField(primary_key=True)
    renewaldate = models.DateField()
    renewalperiod = models.CharField(max_length=100)
    lease_id= models.ForeignKey('leaserenewal.leaserenewal',related_name= 'id+',null=True, default=None,on_delete=models.CASCADE)