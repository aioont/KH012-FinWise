# Generated by Django 3.1.4 on 2024-02-04 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_investment_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
