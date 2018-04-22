# Generated by Django 2.0.4 on 2018-04-16 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wateringApp', '0002_auto_20180414_1038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statistics',
            options={'ordering': ['dataPub']},
        ),
        migrations.AlterField(
            model_name='statistics',
            name='dataPub',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='sensor',
            field=models.CharField(choices=[('temperature', 'temperature'), ('waterContent', 'water content'), ('lumen', 'lumen')], default='temperature', max_length=15),
        ),
    ]