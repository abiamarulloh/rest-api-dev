# Generated by Django 4.1.3 on 2022-12-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShahihBukharis',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('kitab', models.CharField(max_length=200)),
                ('arab', models.TextField()),
                ('terjemah', models.TextField()),
            ],
            options={
                'db_table': 'shahih_bukharis',
                'managed': False,
            },
        ),
    ]