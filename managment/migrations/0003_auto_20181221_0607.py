# Generated by Django 2.1.4 on 2018-12-21 06:07

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0002_property_property_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='email',
            field=models.EmailField(default='True', max_length=254),
        ),
        migrations.AddField(
            model_name='owner',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(default='True', max_length=128),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_img',
            field=models.ImageField(blank=True, null=True, upload_to='property_img/'),
        ),
    ]