# Generated by Django 4.2.5 on 2024-02-29 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_rename_messages_contact_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
    ]
