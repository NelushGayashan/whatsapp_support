# Generated by Django 5.1.5 on 2025-01-25 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('sent', 'Sent'), ('failed', 'Failed')], default='sent', max_length=10),
        ),
    ]