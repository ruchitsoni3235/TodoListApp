# Generated by Django 5.2 on 2025-04-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='item',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
