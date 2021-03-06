# Generated by Django 4.0.2 on 2022-03-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfetcherapp', '0015_alter_article_download_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendationserving',
            old_name='ready_for_viewing',
            new_name='is_being_prepared',
        ),
        migrations.RemoveField(
            model_name='recommendationtopic',
            name='topic_method',
        ),
        migrations.AddField(
            model_name='currentlyfetchedarticle',
            name='tfidf',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='recommendationserving',
            name='blacklisted_articles_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recommendationserving',
            name='topic_clustering_method',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='blacklist',
            name='keyword',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blacklist',
            name='lemmatized',
            field=models.TextField(),
        ),
    ]
