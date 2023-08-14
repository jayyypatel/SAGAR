# Generated by Django 3.2.7 on 2022-06-25 05:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150)),
                ('message', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]