# Generated by Django 2.1.7 on 2019-03-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminar',
            name='hours_number',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Академических часов'),
        ),
    ]
