# Generated by Django 4.2.8 on 2024-02-27 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created',
        ),
    ]
