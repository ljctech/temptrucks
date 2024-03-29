# Generated by Django 2.0.7 on 2019-01-11 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saferdb', '0015_remove_nyactivecorp_dotnmb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nyactivecorp',
            name='CEOAddress1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='CEOAddress2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='CEOCity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='CEOName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='CEOState',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='CEOZip',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='County',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='CurrentEntityName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='DOSProcessAddress1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='DOSProcessAddress2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='DOSProcessCity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='DOSProcessName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='DOSProcessState',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='DOSProcessZip',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='EntityType',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='InitialDOSFilingDate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='Jurisdiction',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='LocationAddress1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='LocationAddress2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='LocationCity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='LocationName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='LocationState',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='LocationZip',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='RegisteredAgentAddress1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='RegisteredAgentAddress2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='RegisteredAgentCity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='RegisteredAgentName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='RegisteredAgentState',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nyactivecorp',
            name='RegisteredAgentZip',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
