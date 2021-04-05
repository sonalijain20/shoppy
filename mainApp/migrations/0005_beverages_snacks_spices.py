# Generated by Django 3.1.7 on 2021-04-05 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20210404_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField()),
                ('gm100', models.BooleanField(blank=True, default=None, null=True)),
                ('gm100_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('gm250', models.BooleanField(blank=True, default=None, null=True)),
                ('gm250_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('gm500', models.BooleanField(blank=True, default=None, null=True)),
                ('gm500_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('kg1', models.BooleanField(blank=True, default=None, null=True)),
                ('kg1_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('seller_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Snacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField()),
                ('gm100', models.BooleanField(blank=True, default=None, null=True)),
                ('gm100_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('gm250', models.BooleanField(blank=True, default=None, null=True)),
                ('gm250_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('gm500', models.BooleanField(blank=True, default=None, null=True)),
                ('gm500_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('kg1', models.BooleanField(blank=True, default=None, null=True)),
                ('kg1_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('img1', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('seller_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Beverages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('finalPrice', models.IntegerField()),
                ('l100', models.BooleanField(blank=True, default=None, null=True)),
                ('l100_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('l250', models.BooleanField(blank=True, default=None, null=True)),
                ('l250_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('l500', models.BooleanField(blank=True, default=None, null=True)),
                ('l500_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('l1_quan', models.IntegerField(blank=True, default=0, null=True)),
                ('l1', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('img2', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('img3', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('seller_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.seller')),
            ],
        ),
    ]
