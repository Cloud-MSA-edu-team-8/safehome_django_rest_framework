# Generated by Django 3.1 on 2020-09-01 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draw_data',
            fields=[
                ('region_code', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('district_color', models.CharField(max_length=1000)),
                ('svgd', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_code', models.CharField(default='', max_length=30, primary_key=True, serialize=False)),
                ('region_name', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Alcohol',
            fields=[
                ('region_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='safehome.region', unique=True)),
                ('accident_num', models.IntegerField(default=0)),
                ('dead_num', models.IntegerField(default=0)),
                ('casual_num', models.IntegerField(default=0)),
                ('acc_rate', models.IntegerField(default=0)),
                ('casual_rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('region_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='safehome.region', unique=True)),
                ('accident_num', models.IntegerField(default=0)),
                ('accident_rate', models.IntegerField(default=0)),
                ('safe_num', models.IntegerField(default=0)),
                ('safe_rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('region_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='safehome.region', unique=True)),
                ('murder', models.IntegerField()),
                ('robber', models.IntegerField()),
                ('rape', models.IntegerField()),
                ('theft', models.IntegerField()),
                ('violence', models.IntegerField()),
                ('total', models.IntegerField()),
                ('arr_total', models.IntegerField()),
                ('arrest', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fire_damage',
            fields=[
                ('region_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='safehome.region', unique=True)),
                ('fire_damage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Flood',
            fields=[
                ('region_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='safehome.region', unique=True)),
                ('people', models.IntegerField(default=0)),
                ('houses', models.IntegerField(default=0)),
                ('buildings', models.IntegerField(default=0)),
                ('public', models.IntegerField(default=0)),
                ('total_cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('region_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='safehome.region', unique=True)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('region_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='safehome.region', unique=True)),
                ('household', models.IntegerField(default=0)),
                ('total_male', models.IntegerField(default=0)),
                ('total_female', models.IntegerField(default=0)),
                ('total_total', models.IntegerField(default=0)),
                ('kor_male', models.IntegerField(default=0)),
                ('kor_female', models.IntegerField(default=0)),
                ('kor_total', models.IntegerField(default=0)),
                ('for_male', models.IntegerField(default=0)),
                ('for_female', models.IntegerField(default=0)),
                ('for_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('region_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='safehome.region', unique=True)),
                ('population', models.IntegerField(default=0)),
                ('flood_vic', models.IntegerField(default=0)),
                ('crime_num', models.IntegerField(default=0)),
                ('crime_arr', models.IntegerField(default=0)),
                ('fire_cost', models.IntegerField(default=0)),
                ('child_car_num', models.IntegerField(default=0)),
                ('alc_car_num', models.IntegerField(default=0)),
                ('house_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Total_rate',
            fields=[
                ('region_code', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='safehome.region', unique=True)),
                ('population_rate', models.IntegerField(default=0)),
                ('population', models.IntegerField(default=0)),
                ('flood_vic_rate', models.IntegerField(default=0)),
                ('flood_vic', models.IntegerField(default=0)),
                ('crime_num_rate', models.IntegerField(default=0)),
                ('crime_num', models.IntegerField(default=0)),
                ('crime_arr', models.IntegerField(default=0)),
                ('fire_cost_rate', models.IntegerField(default=0)),
                ('fire_cost', models.IntegerField(default=0)),
                ('child_car_rate', models.IntegerField(default=0)),
                ('child_car_num', models.IntegerField(default=0)),
                ('alc_car_rate', models.IntegerField(default=0)),
                ('alc_car_num', models.IntegerField(default=0)),
                ('house_price_rate', models.IntegerField(default=0)),
                ('house_price', models.IntegerField(default=0)),
            ],
        ),
    ]
