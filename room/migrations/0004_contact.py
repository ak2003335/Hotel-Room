# Generated by Django 3.1.6 on 2021-11-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_name', models.CharField(max_length=20, null=True)),
                ('con_mobile', models.CharField(max_length=30, null=True)),
                ('con_email', models.CharField(max_length=10, null=True)),
                ('con_purpose', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
