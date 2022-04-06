# Generated by Django 3.0.5 on 2021-05-17 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('_id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('team', models.CharField(max_length=50)),
                ('facility', models.CharField(max_length=150)),
                ('startDateTime', models.DateTimeField()),
                ('endDateTime', models.DateTimeField()),
            ],
        ),
    ]