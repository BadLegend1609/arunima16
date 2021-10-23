# Generated by Django 3.2.5 on 2021-10-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_header_1', models.CharField(blank=True, default='Header 1', max_length=200, null=True)),
                ('page_sub_header_1', models.CharField(blank=True, default='Sub Header 1', max_length=200, null=True)),
                ('page_header_2', models.CharField(blank=True, default='Header 2', max_length=200, null=True)),
                ('page_sub_header_2', models.CharField(blank=True, default='Sub Header 2', max_length=200, null=True)),
                ('page_header_3', models.CharField(blank=True, default='Header 3', max_length=200, null=True)),
                ('page_sub_header_3', models.CharField(blank=True, default='Sub Header 3', max_length=200, null=True)),
                ('who_am_i', models.TextField(blank=True, default='Lorem ipsum dolor sit amet set, consectetur utes anet adipisicing elit, sed do eiusmod tempor incidist.', max_length=5000, null=True)),
                ('what_am_i', models.TextField(blank=True, default='Lorem ipsum dolor sit amet set, consectetur utes anet adipisicing elit, sed do eiusmod tempor incidist.', max_length=5000, null=True)),
                ('why_i_do_it', models.TextField(blank=True, default='Lorem ipsum dolor sit amet set, consectetur utes anet adipisicing elit, sed do eiusmod tempor incidist.', max_length=5000, null=True)),
                ('since_when', models.TextField(blank=True, default='Lorem ipsum dolor sit amet set, consectetur utes anet adipisicing elit, sed do eiusmod tempor incidist.', max_length=5000, null=True)),
            ],
        ),
    ]
