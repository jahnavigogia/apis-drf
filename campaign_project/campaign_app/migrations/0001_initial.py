# Generated by Django 5.1.4 on 2024-12-07 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=100)),
                ('voice_id', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('campaign_type', models.CharField(choices=[('Inbound', 'Inbound'), ('Outbound', 'Outbound')], max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Paused', 'Paused'), ('Completed', 'Completed')], max_length=10)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='campaign_app.agent')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('result_type', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('cost', models.FloatField()),
                ('outcome', models.CharField(max_length=255)),
                ('call_duration', models.FloatField()),
                ('recording', models.URLField()),
                ('summary', models.TextField()),
                ('transcription', models.TextField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='campaign_app.campaign')),
            ],
        ),
    ]
