# Generated by Django 3.1.3 on 2022-07-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('High', 'High'), ('Average', 'Average')], default='Average', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('High', 'High'), ('Average', 'Average')], default='Average', max_length=100, null=True),
        ),
    ]
