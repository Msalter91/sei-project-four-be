# Generated by Django 4.0.1 on 2022-01-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_cats',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='has_dogs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='has_kids',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='preferred_age',
            field=models.CharField(default='one', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='preferred_breed_one',
            field=models.CharField(default='lab', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='preferred_breed_three',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='preferred_breed_two',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='preferred_sex',
            field=models.CharField(default='male', max_length=30),
            preserve_default=False,
        ),
    ]