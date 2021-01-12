# Generated by Django 3.1.3 on 2020-11-25 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.BigIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Profile',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('cashondelivery', 'Cash on Delivery')], default='cashondelivery', max_length=50)),
                ('amount', models.IntegerField()),
                ('transaction_date', models.DateField()),
                ('cylinder_type', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_no', models.CharField(max_length=50)),
                ('aadhar_image', models.ImageField(upload_to='user_document/%Y-%m')),
                ('rationcard_no', models.CharField(max_length=50)),
                ('rationcard_image', models.ImageField(upload_to='user_document/%Y-%m')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Documents',
            },
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='', max_length=20)),
                ('dob', models.DateField()),
                ('relative', models.CharField(default='', max_length=50)),
                ('ffname', models.CharField(default='', max_length=50)),
                ('fmname', models.CharField(default='', max_length=50)),
                ('flname', models.CharField(default='', max_length=50)),
                ('mfname', models.CharField(default='', max_length=50)),
                ('mmname', models.CharField(default='', max_length=50)),
                ('mlname', models.CharField(default='', max_length=50)),
                ('costomer_no', models.CharField(default='', max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('canceled', 'Canceled')], default='pending', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Gas Connection',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cylinder_type', models.CharField(choices=[('14.2', '14.2 Kg'), ('5', '5Kg')], default='5', max_length=50)),
                ('price', models.IntegerField()),
                ('book_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('canceled', 'Canceled')], default='pending', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.connection')),
            ],
            options={
                'verbose_name_plural': 'Gas Booking',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='', max_length=50)),
                ('district', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('pincode', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Address',
            },
        ),
    ]
