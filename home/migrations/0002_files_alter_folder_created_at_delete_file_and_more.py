# Generated by Django 4.2 on 2023-04-26 13:50

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=home.models.get_upload_path)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='folder',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.AddField(
            model_name='files',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.folder'),
        ),
    ]
