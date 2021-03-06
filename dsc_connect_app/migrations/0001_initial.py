# Generated by Django 3.0.2 on 2020-02-28 14:12

import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import dsc_connect_app.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(max_length=10, unique=True, verbose_name='phone number')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('gender', models.CharField(blank=True, max_length=8, verbose_name='gender')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_worker', models.BooleanField(default=False, verbose_name='worker')),
                ('is_volunteer', models.BooleanField(default=False, verbose_name='volunteer')),
                ('is_online', models.BooleanField(default=False, verbose_name='online')),
                ('last_activity', models.DateTimeField(default=datetime.date.today, verbose_name='last activity')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('otp', models.CharField(default=True, max_length=4)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', dsc_connect_app.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Dsc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'draft'), ('1', 'published')], default='draft', max_length=1)),
                ('lead', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=50)),
                ('quote', models.CharField(max_length=512)),
                ('domains', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=512), size=None)),
                ('gmail', models.EmailField(blank=True, max_length=254)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=256)),
                ('team_size', models.IntegerField()),
                ('established_on', models.DateField()),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('website', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('medium', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('behance', models.URLField(blank=True)),
                ('custom', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(blank=True), size=None)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
