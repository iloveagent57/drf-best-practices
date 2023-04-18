# Generated by Django 3.2.18 on 2023-04-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_membership'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the Tag.', max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='quickstart.Tag'),
        ),
    ]