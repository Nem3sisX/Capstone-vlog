# Generated by Django 3.2 on 2021-04-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('dish_type', models.CharField(max_length=100)),
                ('cuisine', models.CharField(max_length=100)),
                ('seasonal', models.BooleanField(default=False)),
                ('allergens', models.BooleanField(default=False)),
                ('advance', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='pics')),
                ('comments', models.TextField()),
            ],
            options={
                'db_table': 'Rest',
            },
        ),
    ]