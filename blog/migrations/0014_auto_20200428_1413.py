# Generated by Django 3.0.5 on 2020-04-28 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200428_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='user',
        ),
    ]
