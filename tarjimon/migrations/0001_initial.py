# Generated by Django 4.0.2 on 2022-08-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inglizcha', models.CharField(max_length=30, verbose_name='Inglizcha')),
                ('uzbekcha', models.CharField(max_length=30, verbose_name='Uzbekcha')),
            ],
        ),
    ]
