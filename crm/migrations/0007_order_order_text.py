# Generated by Django 4.1.3 on 2022-11-15 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_alter_order_order_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_text',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Комментарий'),
        ),
    ]