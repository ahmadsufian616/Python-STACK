# Generated by Django 2.2.4 on 2021-05-23 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auther_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auther',
            name='notes',
        ),
    ]
