# Generated by Django 4.2.5 on 2023-09-12 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_userprofile_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_text',
            new_name='full_text',
        ),
    ]
