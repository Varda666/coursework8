# Generated by Django 4.2.8 on 2023-12-13 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useful_habits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='email', verbose_name='владелец'),
        ),
    ]