# Generated by Django 3.1 on 2021-09-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=77)),
                ('last_name', models.CharField(max_length=77)),
                ('username', models.CharField(max_length=77, unique=True)),
                ('email', models.EmailField(max_length=77, unique=True)),
                ('phone_number', models.CharField(max_length=77)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('date_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]