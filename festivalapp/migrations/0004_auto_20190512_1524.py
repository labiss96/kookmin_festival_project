# Generated by Django 2.1.8 on 2019-05-12 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('festivalapp', '0003_auto_20190512_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lost',
            old_name='bod2y',
            new_name='body2',
        ),
    ]