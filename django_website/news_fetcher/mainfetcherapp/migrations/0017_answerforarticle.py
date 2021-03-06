# Generated by Django 4.0.2 on 2022-03-30 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainfetcherapp', '0016_rename_ready_for_viewing_recommendationserving_is_being_prepared_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerForArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('certainty', models.FloatField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainfetcherapp.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
