# Generated by Django 3.0.3 on 2020-03-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0007_auto_20200221_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='comment',
            field=models.CharField(blank=True, help_text='Comment for this case.', max_length=256, verbose_name='Comment'),
        ),
    ]