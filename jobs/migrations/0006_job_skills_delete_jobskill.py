# Generated by Django 4.2.2 on 2023-08-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_job_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='JobSkill',
        ),
    ]