# Generated by Django 3.2.2 on 2023-11-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persontoperson', '0002_birthchartdb_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthchartdb',
            name='As',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='birthchartdb',
            name='Ju',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='birthchartdb',
            name='Ke',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='birthchartdb',
            name='Ma',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='birthchartdb',
            name='Me',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='birthchartdb',
            name='Mo',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='birthchartdb',
            name='Ra',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='birthchartdb',
            name='Sa',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='birthchartdb',
            name='Su',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='birthchartdb',
            name='Ve',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
