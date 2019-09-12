# Generated by Django 2.2.4 on 2019-09-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0005_submission_archive_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='_state',
            field=models.CharField(choices=[('new', 'New'), ('running', 'Running'), ('done', 'Done')], default='new', max_length=32),
        ),
        migrations.AddField(
            model_name='submission',
            name='vmck_id',
            field=models.IntegerField(null=True),
        ),
    ]