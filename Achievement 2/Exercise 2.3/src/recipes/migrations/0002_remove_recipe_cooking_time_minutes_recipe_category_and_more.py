from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        # Align field names with simplified model
        migrations.RenameField(
            model_name='recipe',
            old_name='cooking_time_minutes',
            new_name='cooking_time',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(help_text='Comma-separated list of ingredients'),
        ),
    ]
