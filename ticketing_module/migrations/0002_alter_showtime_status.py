# Generated by Django 4.1.5 on 2023-07-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='status',
            field=models.IntegerField(choices=[(1, 'sale not started'), (2, 'sale open'), (3, 'tickets sold'), (4, 'sale closed'), (5, 'movie played'), (6, 'show canceled')]),
        ),
    ]