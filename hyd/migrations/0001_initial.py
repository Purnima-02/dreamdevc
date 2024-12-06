# Generated by Django 4.2.16 on 2024-12-02 11:42

from django.db import migrations, models
import hyd.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='custmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_id', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DSATicket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_type', models.CharField(choices=[('Technical', 'Technical'), ('Billing', 'Billing'), ('General', 'General'), ('Personal', 'Personal'), ('Others', 'Others')], max_length=20)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Open', 'Open'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='New', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25, validators=[hyd.models.validate_only_letters])),
                ('phone_number', models.CharField(max_length=15, validators=[hyd.models.validate_mobile_number])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[hyd.models.validate_email])),
            ],
        ),
        migrations.CreateModel(
            name='FranchiseeTicket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_type', models.CharField(choices=[('Technical', 'Technical'), ('Billing', 'Billing'), ('General', 'General'), ('Personal', 'Personal'), ('Others', 'Others')], max_length=20)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Open', 'Open'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='New', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, validators=[hyd.models.validate_only_letters])),
                ('phone_number', models.CharField(max_length=15, validators=[hyd.models.validate_mobile_number])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[hyd.models.validate_email])),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, validators=[hyd.models.validate_only_letters])),
                ('phone_number', models.CharField(max_length=15, validators=[hyd.models.validate_mobile_number])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[hyd.models.validate_email])),
                ('issue_type', models.CharField(choices=[('personal loan', 'Personal Loan'), ('educational loan', 'Educational Loan'), ('car loan', 'Car Loan'), ('business loan', 'Business Loan'), ('Loan Against Property', 'Loan Against Property'), ('CreditCard', 'Credit Card'), ('Insurance', 'Insurance'), ('Other Loan', 'Other Loan')], max_length=100)),
                ('description', models.TextField()),
                ('related_application_number', models.CharField(blank=True, max_length=100, null=True)),
                ('supporting_documents', models.FileField(blank=True, null=True, upload_to='supporting_documents/')),
                ('status', models.CharField(choices=[('New', 'New'), ('Open', 'Open'), ('In Progress', 'In Progress'), ('Closed', 'Closed')], default='New', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
