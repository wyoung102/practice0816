# Generated by Django 3.2.5 on 2021-07-29 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20210722_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]