# Generated by Django 3.1.2 on 2020-10-30 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('cateory', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='menu/images')),
            ],
        ),
    ]
