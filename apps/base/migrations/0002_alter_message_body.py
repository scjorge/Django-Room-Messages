# Generated by Django 4.0.4 on 2022-06-06 01:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
