# Generated by Django 4.1.3 on 2022-11-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_cmsslider_cms_css'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_img',
            field=models.ImageField(upload_to='sliderimg/', verbose_name='Фото'),
        ),
    ]
