# Generated by Django 4.2 on 2023-04-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0007_rename_user_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(max_length=20),
        ),
    ]
