# Generated by Django 4.2.5 on 2023-10-16 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_bode_post_body_alter_post_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coments',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.post'),
        ),
    ]
