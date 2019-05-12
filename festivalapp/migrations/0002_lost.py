# Generated by Django 2.1.8 on 2019-05-12 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
    ]
