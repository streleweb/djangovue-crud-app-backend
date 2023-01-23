# Generated by Django 3.2 on 2023-01-21 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_user_id_note_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('text', models.CharField(max_length=255)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.note')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]