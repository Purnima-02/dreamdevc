# Generated by Django 5.0.6 on 2024-12-06 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hyd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='supporting_documents',
        ),
    ]