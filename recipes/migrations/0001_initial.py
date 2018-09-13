# Generated by Django 2.1 on 2018-09-07 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispenser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], unique=True)),
                ('is_empty', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(help_text='In milliliter [mL]')),
                ('number', models.PositiveSmallIntegerField(help_text='The number in which order the dose must be served')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('alcohol_percentage', models.FloatField(help_text='Should be between 0 and 100')),
                ('density', models.FloatField(default=1000, help_text='In grams per liter [g/L]')),
            ],
        ),
        migrations.CreateModel(
            name='Mix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('likes', models.PositiveSmallIntegerField(default=0)),
                ('mixed', models.PositiveSmallIntegerField(default=0)),
                ('ingredients', models.ManyToManyField(related_name='in_mixes', through='recipes.Dose', to='recipes.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='dose',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Ingredient'),
        ),
        migrations.AddField(
            model_name='dose',
            name='mix',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Mix'),
        ),
        migrations.AddField(
            model_name='dispenser',
            name='ingredient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.Ingredient'),
        ),
    ]