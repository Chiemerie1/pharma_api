# Generated by Django 4.1.7 on 2023-03-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='code',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]