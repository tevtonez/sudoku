# Generated by Django 2.1.4 on 2018-12-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku_app', '0007_auto_20181207_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudokumodel',
            name='board_data',
            field=models.CharField(blank=True, max_length=345, null=True),
        ),
    ]
