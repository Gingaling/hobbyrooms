# Generated by Django 4.0.4 on 2023-02-15 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_room_participants'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Misc',
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
