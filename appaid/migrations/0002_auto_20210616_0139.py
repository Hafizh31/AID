# Generated by Django 3.2.4 on 2021-06-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appaid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penyakit',
            name='pencegahan',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='penyakit',
            name='penyebab',
            field=models.CharField(max_length=10000),
        ),
    ]
