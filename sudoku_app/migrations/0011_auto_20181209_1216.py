# Generated by Django 2.1.4 on 2018-12-09 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku_app', '0010_counterclass'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CounterClass',
            new_name='CounterModel',
        ),
    ]