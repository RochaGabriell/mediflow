# Generated by Django 5.1 on 2024-09-08 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.TextField(verbose_name='Diagnosis')),
                ('prescription', models.TextField(verbose_name='Prescription')),
                ('documents', models.FileField(blank=True, null=True, upload_to='medical_records/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Medical Record',
                'verbose_name_plural': 'Medical Records',
            },
        ),
    ]
