# Generated by Django 4.1.5 on 2023-07-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
