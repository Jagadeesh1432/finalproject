# Generated by Django 2.2.5 on 2019-11-08 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('Account_Number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Branch', models.CharField(max_length=40)),
                ('profile_pic', models.ImageField(blank=True, upload_to='user')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
