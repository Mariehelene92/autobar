# Generated by Django 2.1 on 2018-09-13 11:16

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20180912_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='mix',
            name='image',
            field=models.ImageField(height_field='height', max_length=200, null=True, upload_to=recipes.models.mix_upload_to, width_field='width'),
        ),
    ]
