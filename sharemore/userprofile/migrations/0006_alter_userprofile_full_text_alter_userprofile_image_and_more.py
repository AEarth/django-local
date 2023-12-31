# Generated by Django 4.2.5 on 2023-09-14 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_rename_profile_text_userprofile_full_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='full_text',
            field=models.TextField(blank=True, null=True, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/item_images/', verbose_name='Profile Pic'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_url',
            field=models.URLField(blank=True, null=True, verbose_name='Social URL'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='summary',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Catch Phrase'),
        ),
    ]
