# Generated by Django 3.2.18 on 2023-04-12 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0001_create_pub_and_article_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='owner',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(help_text='The User who authored the Article.', on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication',
            field=models.ForeignKey(help_text='The publication in which this Article is published.', on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='quickstart.publication'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='The title of the Article.', max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='name',
            field=models.CharField(help_text='The name of the publication.', max_length=1024, unique=True),
        ),
        migrations.CreateModel(
            name='PublicationMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], help_text="The user's role as a member of the publication.", max_length=512)),
                ('publication', models.ForeignKey(help_text='The publication to which the member belongs.', on_delete=django.db.models.deletion.CASCADE, related_name='members', to='quickstart.publication')),
                ('user', models.ForeignKey(help_text='The User record associated with this membership.', on_delete=django.db.models.deletion.CASCADE, related_name='membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
