# Generated by Django 5.1.1 on 2024-12-25 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_weeklyquiz_quizquestion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizquestion',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
