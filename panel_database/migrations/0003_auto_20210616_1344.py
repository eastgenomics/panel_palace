# Generated by Django 3.1.4 on 2021-06-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_database', '0002_auto_20210518_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='panelapp_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='panelfeatures',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]