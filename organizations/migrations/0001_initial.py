# Generated by Django 4.2.3 on 2023-11-29 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=16, unique=True)),
                ('name', models.CharField(blank=True, max_length=64)),
                ('description', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('contact', models.JSONField(blank=True, default=dict)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('joined_date', models.DateTimeField(null=True)),
                ('role', models.CharField(choices=[('worker', 'Worker'), ('supervisor', 'Supervisor'), ('maintainer', 'Maintainer'), ('owner', 'Owner')], max_length=16)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='organizations.organization')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
                'unique_together': {('user', 'organization')},
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('key', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('sent_date', models.DateTimeField(null=True)),
                ('membership', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='organizations.membership')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]
