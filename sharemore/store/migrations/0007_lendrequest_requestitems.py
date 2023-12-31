# Generated by Django 4.2.5 on 2023-09-11 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0006_item_image_med'),
    ]

    operations = [
        migrations.CreateModel(
            name='LendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pickup_date', models.DateField(help_text='Anticipated pickup day')),
                ('return_date', models.DateField(help_text='Anticipated return day')),
                ('status', models.CharField(choices=[('p', 'Pending'), ('a', 'Approved'), ('d', 'Denied')], default='p', max_length=1)),
                ('requester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requester', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
                ('lend_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lend_request', to='store.lendrequest')),
            ],
        ),
    ]
