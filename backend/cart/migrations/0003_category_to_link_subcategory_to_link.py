# Generated by Django 4.2.1 on 2023-05-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_subcategory_options_category_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='to_link',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='to_link'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='to_link',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='to_link'),
        ),
    ]