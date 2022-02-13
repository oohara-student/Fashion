# Generated by Django 4.0.1 on 2022-01-31 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='服ジャンル')),
            ],
        ),
        migrations.CreateModel(
            name='Kinds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='服種類')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(default=0, verbose_name='サイズ')),
                ('pattern', models.BooleanField(verbose_name='柄')),
                ('color', models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name='服カラー')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webtestapp.genre')),
                ('kinds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webtestapp.kinds')),
            ],
        ),
    ]
