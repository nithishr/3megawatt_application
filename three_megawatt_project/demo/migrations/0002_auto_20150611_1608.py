# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('a_value', models.DecimalField(max_digits=6, decimal_places=3)),
                ('b_value', models.DecimalField(max_digits=6, decimal_places=3)),
            ],
        ),
        migrations.RenameModel(
            old_name='Sites',
            new_name='Site',
        ),
        migrations.RemoveField(
            model_name='sitedetails',
            name='site',
        ),
        migrations.DeleteModel(
            name='SiteDetails',
        ),
        migrations.AddField(
            model_name='sitedetail',
            name='site',
            field=models.ForeignKey(to='demo.Site'),
        ),
    ]
