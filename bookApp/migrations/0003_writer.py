# Generated by Django 4.1.7 on 2023-04-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0002_book_writer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
            ],
        ),
    ]
