# Generated by Django 2.0.3 on 2018-03-17 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age_Restriction', models.IntegerField()),
                ('year_of_publish', models.DateField()),
                ('Platform', models.CharField(max_length=200)),
                ('Quantity', models.IntegerField()),
                ('Game_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Product')),
            ],
        ),
    ]
