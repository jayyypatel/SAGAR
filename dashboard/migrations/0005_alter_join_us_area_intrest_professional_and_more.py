# Generated by Django 4.0.6 on 2022-07-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_publication_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join_us',
            name='area_intrest_professional',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='join_us',
            name='area_intrest_social',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]