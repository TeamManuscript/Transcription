from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0002_discussion_thum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='thum',
            new_name='thumb',
        ),
    ]
