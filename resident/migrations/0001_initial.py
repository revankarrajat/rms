# Generated by Django 2.1.4 on 2018-12-15 10:53

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resident',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('res_firstname', models.CharField(max_length=100)),
                ('res_lastname', models.CharField(max_length=100)),
                ('res_email_id', models.EmailField(max_length=254)),
                ('res_landline_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('res_phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('notes', models.TextField()),
                ('attachment', models.FileField(upload_to='')),
            ],
        ),
    ]
