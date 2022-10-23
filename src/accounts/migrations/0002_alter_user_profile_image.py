# Generated by Django 4.1.2 on 2022-10-23 15:29

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', help_text='size of logo must be 250*250 and format must be png image file', keep_meta=True, null=True, quality=75, scale=None, size=[250, 250], upload_to='accounts/images/profiles/'),
        ),
    ]