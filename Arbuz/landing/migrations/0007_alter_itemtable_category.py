# Generated by Django 4.1.7 on 2023-05-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_payment_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtable',
            name='category',
            field=models.CharField(choices=[('fruits', 'Fruits'), ('vegetables', 'Vegetables'), ('drinks', 'Drinks')], default='fruits', max_length=255),
        ),
    ]
