# Generated by Django 2.1.5 on 2019-02-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pousada', '0006_auto_20190224_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casadepedracotacao',
            name='dialy_of_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='casadepedracotacao',
            name='portion',
            field=models.IntegerField(),
        ),
    ]
