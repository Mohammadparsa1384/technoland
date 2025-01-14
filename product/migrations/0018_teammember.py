# Generated by Django 5.0.1 on 2024-03-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_rename_user_commentproduct_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='team')),
                ('name', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
    ]
