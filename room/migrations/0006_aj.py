# Generated by Django 3.2.5 on 2022-02-17 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_booked'),
    ]

    operations = [
        migrations.CreateModel(
            name='aj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(max_length=1000, null=True)),
                ('y', models.IntegerField(max_length=1000, null=True)),
            ],
        ),
    ]