# Generated by Django 4.2.9 on 2024-03-06 04:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pexpo", "0011_course_student_enrollment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=models.CharField(
                max_length=13,
                validators=[django.core.validators.MinLengthValidator(13)],
            ),
        ),
    ]
