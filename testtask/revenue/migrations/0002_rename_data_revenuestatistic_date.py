# Generated by Django 4.2.5 on 2023-09-28 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revenuestatistic',
            old_name='data',
            new_name='date',
        ),
    ]
