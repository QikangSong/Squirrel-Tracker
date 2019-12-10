# Generated by Django 2.2.7 on 2019-12-06 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('latitude', models.FloatField(help_text='Latitude of Sighting')),
                ('longitude', models.FloatField(help_text='Longitude of Sighting')),
                ('squirrel_id', models.CharField(help_text="Unique Squirrel ID. If the ID already exist, sighting won't be add", max_length=32, primary_key=True, serialize=False)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='Sighting session', max_length=2)),
                ('date', models.DateField(help_text='Sighting date in YYYY-MM-DD format')),
                ('age', models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('', '')], default='adult', help_text='Age of Squirrel', max_length=16, null=True)),
                ('fur_color', models.CharField(choices=[('gray', 'Gray'), ('black', 'Black'), ('cinnamon', 'Cinnamon'), ('', '')], default='gray', help_text='Fur color of Squirrel', max_length=10, null=True)),
                ('location', models.CharField(choices=[('ground_plane', 'Ground_Plane'), ('above_ground', 'Above_Ground'), ('', '')], default='ground_plane', help_text='Location of Squirrel', max_length=20, null=True)),
                ('specific_location', models.CharField(blank=True, help_text='Specific location of Squirrel', max_length=20, null=True)),
                ('running', models.BooleanField(default=False)),
                ('chasing', models.BooleanField(default=False)),
                ('climbing', models.BooleanField(default=False)),
                ('eating', models.BooleanField(default=False)),
                ('foraging', models.BooleanField(default=False)),
                ('other_activities', models.CharField(blank=True, help_text='Other activity', max_length=20, null=True)),
                ('kuks', models.BooleanField(default=False)),
                ('quaas', models.BooleanField(default=False)),
                ('moans', models.BooleanField(default=False)),
                ('tail_flags', models.BooleanField(default=False)),
                ('tail_twitches', models.BooleanField(default=False)),
                ('approaches', models.BooleanField(default=False)),
                ('indifferent', models.BooleanField(default=False)),
                ('runs_from', models.BooleanField(default=False)),
            ],
        ),
    ]
