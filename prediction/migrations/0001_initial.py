# Generated by Django 4.1 on 2022-12-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Traduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('texte', models.CharField(max_length=50, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]