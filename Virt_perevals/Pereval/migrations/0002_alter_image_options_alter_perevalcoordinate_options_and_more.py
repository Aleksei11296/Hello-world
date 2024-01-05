# Generated by Django 5.0 on 2024-01-03 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pereval', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AlterModelOptions(
            name='perevalcoordinate',
            options={'verbose_name': 'Координаты', 'verbose_name_plural': 'Координаты'},
        ),
        migrations.AlterModelOptions(
            name='perevallevel',
            options={'verbose_name': 'Уровень', 'verbose_name_plural': 'Уровни'},
        ),
        migrations.AlterField(
            model_name='image',
            name='data',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='connect',
            field=models.TextField(blank=True, null=True, verbose_name='Соединяет'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='coord',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Pereval.perevalcoordinate', verbose_name='Координаты'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pereval.perevallevel', verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='status',
            field=models.CharField(choices=[('NW', 'New'), ('AC', 'Accepted'), ('PN', 'Pending'), ('RJ', 'Rejected')], default='NW', max_length=2, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pereval.perevaluser', verbose_name='Пользователь'),
        ),
    ]