# Generated by Django 4.1.7 on 2023-04-05 14:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("traits", "0002_trait_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trait",
            name="pets",
        ),
    ]
