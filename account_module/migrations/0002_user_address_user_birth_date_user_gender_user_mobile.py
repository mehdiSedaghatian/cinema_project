# Generated by Django 4.1.5 on 2023-07-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'male'), (2, 'male')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
