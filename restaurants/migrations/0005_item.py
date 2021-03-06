# Generated by Django 2.2.13 on 2020-09-07 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurant_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=700)),
                ('price', models.IntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
            ],
        ),
    ]
