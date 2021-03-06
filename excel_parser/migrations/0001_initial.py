# Generated by Django 3.0.7 on 2020-06-27 11:37

from django.db import migrations, models
import excel_parser.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MDA_name', models.CharField(max_length=100)),
                ('project_recipient_name', models.CharField(max_length=120)),
                ('project_name', models.TextField()),
                ('project_amount', models.FloatField()),
                ('project_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ExcelSaverModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_report_file', models.FileField(null=True, upload_to=excel_parser.models.upload_file_handler)),
            ],
        ),
    ]
