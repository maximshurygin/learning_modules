# Generated by Django 5.0 on 2023-12-23 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['id'], 'verbose_name': 'Модуль', 'verbose_name_plural': 'Модули'},
        ),
    ]
