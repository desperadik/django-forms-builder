from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_field_send_to_email_form_email_message_copies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='email_copies',
            field=models.CharField(blank=True, help_text='One or more email addresses, separated by commas', max_length=1000, verbose_name='Send copies to'),
        ),
    ]
