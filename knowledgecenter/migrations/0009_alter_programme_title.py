# Generated by Django 4.0.6 on 2022-07-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgecenter', '0008_student_programme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
