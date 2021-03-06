# Generated by Django 4.0.2 on 2022-04-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0002_remove_services_service_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barber_name', models.CharField(max_length=50, verbose_name='Name')),
                ('work_name', models.CharField(max_length=30, verbose_name='Work name')),
                ('about_barber', models.TextField(verbose_name='About barber')),
                ('barber_photo', models.ImageField(upload_to='', verbose_name='Photo')),
            ],
            options={
                'verbose_name_plural': 'Barbers',
            },
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name_plural': 'FAQ'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Services'},
        ),
    ]
