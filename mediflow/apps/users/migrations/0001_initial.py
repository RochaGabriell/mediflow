# Generated by Django 5.1 on 2024-09-08 03:54

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                 help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                 max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True,
                 max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True,
                 max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True,
                 max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                 help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(
                    default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('receptionist', 'Receptionist'), (
                    'patient', 'Patient')], default='patient', max_length=20, verbose_name='Função')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                 related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                 related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DoctorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(max_length=20, verbose_name='CRM')),
                ('especiality', models.CharField(
                    max_length=255, verbose_name='Especialidade')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
            },
        ),
        migrations.CreateModel(
            name='DoctorAvailabilityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(choices=[(0, 'Segunda-feira'), (1, 'Terça-feira'), (2, 'Quarta-feira'), (
                    3, 'Quinta-feira'), (4, 'Sexta-feira'), (5, 'Sábado'), (6, 'Domingo')], verbose_name='Dia da Semana')),
                ('start_time', models.TimeField(verbose_name='Hora de Início')),
                ('end_time', models.TimeField(verbose_name='Hora de Término')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='availabilities', to='users.doctormodel', verbose_name='Médico')),
            ],
            options={
                'verbose_name': 'Disponibilidade do Médico',
                'verbose_name_plural': 'Disponibilidades do Médico',
                'unique_together': {('doctor', 'day_of_week', 'start_time', 'end_time')},
            },
        ),
    ]
