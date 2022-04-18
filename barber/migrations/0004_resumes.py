# Generated by Django 4.0.2 on 2022-04-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0003_barbers_alter_comments_options_alter_faq_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone')),
                ('summary', models.TextField(verbose_name='Message')),
                ('picture', models.ImageField(upload_to='', verbose_name='Upload Files')),
            ],
            options={
                'verbose_name_plural': 'Resumes',
            },
        ),
    ]
