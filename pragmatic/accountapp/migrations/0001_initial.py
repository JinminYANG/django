# Generated by Django 4.0 on 2022-01-27 01:49

import accountapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='noname_company', max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_updating', models.BooleanField(default=False)),
                ('statistics_updated_at', models.DateTimeField()),
                ('member_updated_at', models.DateTimeField()),
                ('coupon_updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CouponMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_master_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='DBfCompany',
            fields=[
                ('company_seq', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('view_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HelloWorld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('team_color', models.CharField(default='rgba(240, 116, 137, 1)', max_length=25, null=True, verbose_name='COLOR')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(default='noname_id', max_length=200, null=True)),
                ('coupon_id', models.CharField(default='coupon_id', max_length=200, null=True)),
                ('mem_seq', models.IntegerField(null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('total_read_books', models.IntegerField(null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[accountapp.models.min_length_3_validator])),
            ],
        ),
        migrations.CreateModel(
            name='UpdateFromDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.DateTimeField(blank=True, null=True)),
                ('user', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatisticsMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistics_month', models.DateTimeField()),
                ('read_book_count', models.IntegerField(blank=True, null=True)),
                ('avg_read_book_time', models.IntegerField(blank=True, null=True)),
                ('sum_read_book_time', models.IntegerField(blank=True, null=True)),
                ('min_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('max_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('sum_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('avg_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('reg_date', models.DateTimeField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.company')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='StatisticsBestCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistics_month', models.DateTimeField()),
                ('category_seq', models.IntegerField()),
                ('category_depth', models.IntegerField(blank=True, null=True)),
                ('category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('read_book_count', models.IntegerField(blank=True, null=True)),
                ('read_book_percent', models.IntegerField(blank=True, null=True)),
                ('read_book_percent_detail', models.FloatField(blank=True, null=True)),
                ('avg_read_book_time', models.IntegerField(blank=True, null=True)),
                ('min_read_book_time', models.IntegerField(blank=True, null=True)),
                ('max_read_book_time', models.IntegerField(blank=True, null=True)),
                ('sum_read_book_time', models.IntegerField(blank=True, null=True)),
                ('avg_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('min_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('max_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('sum_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('reg_date', models.DateTimeField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='StatisticsBestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistics_month', models.DateTimeField()),
                ('book_seq', models.IntegerField()),
                ('book_name', models.CharField(blank=True, max_length=100, null=True)),
                ('read_book_count', models.IntegerField(blank=True, null=True)),
                ('avg_read_book_time', models.IntegerField(blank=True, null=True)),
                ('min_read_book_time', models.IntegerField(blank=True, null=True)),
                ('max_read_book_time', models.IntegerField(blank=True, null=True)),
                ('sum_read_book_time', models.IntegerField(blank=True, null=True)),
                ('avg_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('min_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('max_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('sum_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('reg_date', models.DateTimeField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistics_month', models.DateTimeField()),
                ('sum_member_count', models.IntegerField(blank=True, null=True)),
                ('avg_read_book_count', models.IntegerField(blank=True, null=True)),
                ('min_read_book_count', models.IntegerField(blank=True, null=True)),
                ('max_read_book_count', models.IntegerField(blank=True, null=True)),
                ('sum_read_book_count', models.IntegerField(blank=True, null=True)),
                ('avg_read_book_time', models.IntegerField(blank=True, null=True)),
                ('min_read_book_time', models.IntegerField(blank=True, null=True)),
                ('max_read_book_time', models.IntegerField(blank=True, null=True)),
                ('sum_read_book_time', models.IntegerField(blank=True, null=True)),
                ('min_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('max_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('sum_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('avg_read_book_percent', models.IntegerField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('reg_date', models.DateTimeField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='CouponPublish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_id', models.CharField(default='coupon_id', max_length=200)),
                ('member_id', models.CharField(blank=True, max_length=200, null=True)),
                ('coupon_use_yn', models.CharField(blank=True, max_length=1, null=True)),
                ('reg_date', models.DateTimeField(blank=True, null=True)),
                ('use_date', models.DateTimeField(blank=True, null=True)),
                ('coupon_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountapp.couponmaster')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='company_seq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accountapp.dbfcompany'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
