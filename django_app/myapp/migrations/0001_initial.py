# Generated by Django 3.2.2 on 2022-12-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.PositiveSmallIntegerField(verbose_name='Roll no.')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('cls', models.CharField(max_length=2, verbose_name='Class')),
                ('total_marks', models.PositiveSmallIntegerField(max_length=500, verbose_name='Total marks')),
                ('is_pass', models.BooleanField(default=True, verbose_name='Pass or Fail ?')),
            ],
        ),
    ]