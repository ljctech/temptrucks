# Generated by Django 2.0.7 on 2019-01-11 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saferdb', '0014_nyactivecorp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nyactivecorp',
            name='DOTNmb',
        ),
    ]
