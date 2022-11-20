# Generated by Django 4.1 on 2022-11-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='Oregon', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='paid_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]
