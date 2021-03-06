# Generated by Django 2.0.4 on 2018-04-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wateringApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='dataPub',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='sensor',
            field=models.CharField(choices=[('temperature', 'temp'), ('waterContent', 'wc'), ('lumen', 'lm')], default='temperature', max_length=15),
        ),
    ]
