# Generated by Django 4.2.5 on 2023-09-12 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_image_userprofile_image_med_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
