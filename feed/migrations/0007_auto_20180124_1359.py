# Generated by Django 2.0.1 on 2018-01-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_auto_20180123_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year')], help_text='Enter your year of study ie.. 2 for 2nd year etc.', max_length=10),
        ),
    ]
