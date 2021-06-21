# Generated by Django 3.1.4 on 2021-06-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_database', '0004_clinicalindicationpanels_version'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='clinicalindication',
            name='clinical_in_version_6ddffd_idx',
        ),
        migrations.RemoveIndex(
            model_name='clinicalindicationpanels',
            name='clinical_in_clinica_9b5ae9_idx',
        ),
        migrations.RemoveField(
            model_name='clinicalindication',
            name='version',
        ),
        migrations.AddIndex(
            model_name='clinicalindicationpanels',
            index=models.Index(fields=['clinical_indication', 'panel', 'version'], name='clinical_in_clinica_e1d03c_idx'),
        ),
    ]