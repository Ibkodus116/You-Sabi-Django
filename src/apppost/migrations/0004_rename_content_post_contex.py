# Generated by Django 4.0.5 on 2022-07-17 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apppost', '0003_alter_post_name_delete_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='contex',
        ),
    ]
