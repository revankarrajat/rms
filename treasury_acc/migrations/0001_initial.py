# Generated by Django 2.1.4 on 2018-12-21 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='treasury_acc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rent_of_month', models.PositiveIntegerField()),
                ('rent_of_year', models.PositiveIntegerField()),
                ('rent_amt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rent_paid_date', models.DateField()),
                ('tenant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenant_id+', to='tenant.tenant')),
            ],
        ),
    ]