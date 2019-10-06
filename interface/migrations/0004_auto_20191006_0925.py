# Generated by Django 2.2.5 on 2019-10-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_assignment_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='review_message',
            field=models.CharField(default='none', max_length=4096),
        ),
        migrations.AlterField(
            model_name='submission',
            name='review_score',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
