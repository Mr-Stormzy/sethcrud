# Generated by Django 3.2.12 on 2023-03-28 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sethcrud', '0003_auto_20230328_1141'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]