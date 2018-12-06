# Generated by Django 2.1.4 on 2018-12-06 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudokumodel',
            name='board_c_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Time'),
        ),
        migrations.AddField(
            model_name='sudokumodel',
            name='board_diffic',
            field=models.CharField(default='0', editable=False, max_length=1),
        ),
        migrations.AddField(
            model_name='sudokumodel',
            name='board_title',
            field=models.CharField(default='1d57ed36-488', editable=False, max_length=12),
        ),
    ]
