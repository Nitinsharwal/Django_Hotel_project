# Generated by Django 4.2 on 2025-07-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_hotel_vendor_business_name_hotel_vendor_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='hotel_description',
            field=models.TextField(default=1, max_length=1200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotels',
            name='hotel_name',
            field=models.CharField(max_length=200),
        ),
    ]
