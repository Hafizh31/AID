# Generated by Django 3.2.4 on 2021-06-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penyakit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenispenyakit', models.CharField(max_length=100)),
                ('penyebab', models.CharField(max_length=100)),
                ('pencegahan', models.CharField(max_length=100)),
            ],
        ),
    ]
