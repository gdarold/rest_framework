# Generated by Django 3.0.5 on 2020-05-03 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0002_endereco_longitude'),
        ('core', '0007_auto_20200502_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco'),
        ),
    ]
