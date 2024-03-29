# Generated by Django 2.2.6 on 2019-10-16 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pousada', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotções_pousadasModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('num_adultos', models.IntegerField(default=2)),
                ('num_crianças', models.IntegerField(default=0)),
                ('pousadas', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Pousada_Booking2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pousada', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogComments',
        ),
        migrations.RemoveField(
            model_name='casadepedracotacao',
            name='dialy_of_price_site',
        ),
        migrations.AlterField(
            model_name='casadepedracotacao',
            name='dialy_of_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=19),
        ),
        migrations.DeleteModel(
            name='CasadePedraFicha',
        ),
    ]
