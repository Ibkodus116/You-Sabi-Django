# Generated by Django 4.0.5 on 2022-07-17 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppost', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creator',
            name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='headline',
            field=models.CharField(max_length=100, verbose_name='Headline'),
        ),
    ]