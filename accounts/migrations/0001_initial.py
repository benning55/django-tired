# Generated by Django 2.2 on 2019-05-01 04:15

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
            name='dayoff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('type', models.CharField(choices=[('0', 'ลากิจ'), ('1', 'ลาป่วย')], max_length=1)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('approve_status', models.CharField(choices=[('0', 'ไม่อนุมัติ'), ('1', 'อนุมัติ'), ('3', 'รออนุมัติ')], max_length=1)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]