# Generated by Django 5.1.4 on 2024-12-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalcHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_number', models.IntegerField()),
                ('second_number', models.IntegerField()),
                ('third_number', models.IntegerField()),
                ('four_number', models.IntegerField()),
                ('first_operation', models.CharField(max_length=1)),
                ('second_operation', models.CharField(max_length=1)),
                ('third_operation', models.CharField(max_length=1)),
                ('result', models.IntegerField()),
            ],
        ),
    ]
