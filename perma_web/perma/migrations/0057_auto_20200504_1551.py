# Generated by Django 2.2.12 on 2020-05-04 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perma', '0056_auto_20200305_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('active', 'Active: user may create links.'), ('inactive', 'Inactive: user may view, but not create, links.')], default='active', max_length=10, null=True)),
                ('status_changed', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_sponsorships', to=settings.AUTH_USER_MODEL)),
                ('registrar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='perma.Registrar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='linkuser',
            name='sponsoring_registrars',
            field=models.ManyToManyField(blank=True, help_text='If set, this user is sponsored by a registrar. Any user can be sponsored by any registrar.', related_name='sponsored_users', through='perma.Sponsorship', to='perma.Registrar'),
        ),
    ]
