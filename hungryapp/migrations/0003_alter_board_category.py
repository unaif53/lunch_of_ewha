# Generated by Django 4.0.2 on 2022-03-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hungryapp', '0002_board_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='category',
            field=models.CharField(choices=[('KOREAN', '한식'), ('WESTERN', '양식'), ('CHINESE', '중식'), ('JAPANESE', '일식'), ('SCHOOL FOOD', '분식'), ('BAKERY', '베이커리'), ('BEVERAGE', '커피음료'), ('OTHERS', '그외')], max_length=200),
        ),
    ]
