# Generated by Django 4.0.6 on 2022-07-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0004_mailbox_m_number_alter_donate_receipt_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='doante_us',
            name='contact',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
