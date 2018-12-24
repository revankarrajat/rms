# Generated by Django 2.1.4 on 2018-12-10 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Apartments', '0001_initial'),
        ('Maintenances', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='accidental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenancedate', models.DateField()),
                ('apartmentno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Flatname+', to='Apartments.Apartments')),
                ('maintenanceid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Apartmentsid+', to='Maintenances.Maintenances')),
            ],
        ),
    ]