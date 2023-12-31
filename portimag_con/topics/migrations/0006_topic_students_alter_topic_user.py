# Generated by Django 4.2.5 on 2023-09-12 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0005_topic_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='konu_takip', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
