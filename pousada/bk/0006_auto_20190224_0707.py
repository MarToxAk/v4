# Generated by Django 2.1.5 on 2019-02-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pousada', '0005_auto_20190224_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casadepedracotacao',
            name='checkout',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='casadepedracotacao',
            name='dialy_of_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='casadepedracotacao',
            name='discount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='casadepedracotacao',
            name='discount_dialy',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='casadepedracotacao',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='casadepedracotacao',
            name='person_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='casadepedracotacao',
            name='portion',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
