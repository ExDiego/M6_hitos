# Generated by Django 4.2 on 2024-05-03 01:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_contactform"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ContactForm",
            new_name="Contacto",
        ),
    ]
