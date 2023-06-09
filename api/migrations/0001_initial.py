# Generated by Django 4.1.7 on 2023-03-16 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=15)),
                ('code', models.SmallIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrugCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DrugClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city')),
            ],
            options={
                'verbose_name_plural': 'Pharmacy',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('availability', models.CharField(choices=[('AV', 'Available'), ('UNAV', 'Unavailable')], max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.drugcategories')),
                ('drug_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.drugclasses')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drugs', to='api.owner')),
            ],
        ),
    ]
