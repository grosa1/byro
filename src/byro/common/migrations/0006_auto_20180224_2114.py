# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-24 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0003_mailtemplate_reply_to'),
        ('common', '0005_configuration_liability_interval'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='leave_member_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='mails.MailTemplate'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='leave_office_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='mails.MailTemplate'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='welcome_member_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='mails.MailTemplate'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='welcome_office_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='mails.MailTemplate'),
        ),
    ]
