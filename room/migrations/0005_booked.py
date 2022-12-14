# Generated by Django 3.1.6 on 2021-11-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('mobile1', models.CharField(max_length=20, null=True)),
                ('mobile2', models.CharField(max_length=20, null=True)),
                ('booking_date', models.CharField(max_length=20, null=True)),
                ('days', models.CharField(max_length=20, null=True)),
                ('price', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
