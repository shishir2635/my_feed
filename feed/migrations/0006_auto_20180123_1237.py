# Generated by Django 2.0.1 on 2018-01-23 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0005_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.CharField(help_text='Enter your branch initials i.e.. CE for civil engineering', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(help_text='Can be left blank!', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(help_text='full name', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(help_text='Enter your year of study ie.. 2 for 2nd year etc.', max_length=10),
        ),
    ]
