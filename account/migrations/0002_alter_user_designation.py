# Generated by Django 4.1.3 on 2022-11-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(max_length=255, verbose_name='Designation'),
        ),
    ]