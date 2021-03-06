# Generated by Django 2.2.6 on 2019-11-02 16:20

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
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_kind', models.CharField(choices=[('C', '의류'), ('D', '서신/서류'), ('E', '가전제품류'), ('F', '과일류'), ('G', '곡물류'), ('M', '한약류'), ('F', '식품류'), ('B', '잡화/서적류'), ('E', '기타')], default='E', max_length=1)),
                ('product_name', models.CharField(default='', max_length=30)),
                ('product_price', models.IntegerField(default=0)),
                ('sender_name', models.CharField(max_length=30)),
                ('sender_phone', models.CharField(max_length=12)),
                ('sender_phone_reservation', models.CharField(max_length=12)),
                ('sender_address', models.TextField()),
                ('requesting_text', models.TextField(blank=True, null=True)),
                ('password', models.CharField(max_length=6)),
                ('recipient_name', models.CharField(max_length=30)),
                ('recipient_phone', models.CharField(max_length=12)),
                ('recipient_address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_advance', models.BooleanField(default=False)),
                ('is_delivering', models.BooleanField(default=False)),
                ('current_lat', models.FloatField(blank=True, null=True)),
                ('current_long', models.FloatField(blank=True, null=True)),
                ('sender_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parcel_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
