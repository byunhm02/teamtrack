# Generated by Django 4.2.14 on 2024-07-18 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('myteam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='matches.team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
