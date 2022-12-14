# Generated by Django 3.1.3 on 2022-07-26 15:49

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
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=230, null=True)),
                ('achievement_point', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('bio', models.TextField(blank=True, null=True)),
                ('workfield', models.CharField(blank=True, max_length=230, null=True)),
                ('number', models.CharField(blank=True, max_length=230, null=True)),
                ('location', models.CharField(blank=True, max_length=230, null=True)),
                ('fb_acc', models.URLField(blank=True, null=True)),
                ('tw_acc', models.URLField(blank=True, null=True)),
                ('Ig_acc', models.URLField(blank=True, null=True)),
                ('git_acc', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
