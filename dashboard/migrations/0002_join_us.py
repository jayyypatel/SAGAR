# Generated by Django 3.2.7 on 2022-06-16 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=100)),
                ('affiliation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('qualification', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('area_intrest_social', models.CharField(max_length=150)),
                ('area_intrest_professional', models.CharField(max_length=150)),
                ('brief_profile', models.CharField(max_length=400)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
