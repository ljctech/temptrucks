# Generated by Django 2.0.7 on 2018-11-13 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saferdb', '0004_auto_20181107_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaliIns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possibleDOT', models.IntegerField()),
                ('legalN', models.CharField(max_length=200)),
                ('dbaName', models.CharField(max_length=200)),
                ('bPhone', models.CharField(max_length=20)),
                ('insCo', models.CharField(max_length=200)),
                ('dateEffective', models.DateField()),
                ('workersComp', models.CharField(max_length=200)),
                ('wcEffectiveDate', models.DateField()),
                ('pFleet', models.IntegerField()),
                ('forhireFleet', models.IntegerField()),
            ],
        ),
    ]
