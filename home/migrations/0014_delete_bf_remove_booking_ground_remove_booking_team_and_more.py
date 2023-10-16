# Generated by Django 4.2.3 on 2023-10-07 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_bf'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BF',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='Ground',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='team',
        ),
        migrations.RemoveField(
            model_name='c_payment',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='c_payment',
            name='team',
        ),
        migrations.RemoveField(
            model_name='coach',
            name='userprofile',
        ),
        migrations.RemoveField(
            model_name='g_payment',
            name='GA',
        ),
        migrations.RemoveField(
            model_name='g_payment',
            name='team',
        ),
        migrations.RemoveField(
            model_name='ground',
            name='g_admin',
        ),
        migrations.RemoveField(
            model_name='groundadmin',
            name='userprofile',
        ),
        migrations.DeleteModel(
            name='JTForm',
        ),
        migrations.RemoveField(
            model_name='team',
            name='C',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='C_payment',
        ),
        migrations.DeleteModel(
            name='Coach',
        ),
        migrations.DeleteModel(
            name='G_payment',
        ),
        migrations.DeleteModel(
            name='Ground',
        ),
        migrations.DeleteModel(
            name='GroundAdmin',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]