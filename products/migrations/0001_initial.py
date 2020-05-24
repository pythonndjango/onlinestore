# Generated by Django 3.0.6 on 2020-05-18 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('shipping_cost', models.FloatField()),
                ('quantity', models.PositiveSmallIntegerField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Manufacturer')),
            ],
        ),
    ]
