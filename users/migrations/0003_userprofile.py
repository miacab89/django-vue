# Generated by Django 3.0.5 on 2020-10-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='profiles-images')),
                ('fb_profile', models.CharField(max_length=100)),
                ('twitter_profile', models.CharField(max_length=100)),
                ('linkedin_profile', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
            ],
        ),
    ]