# Generated by Django 2.2.19 on 2021-04-05 22:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0115_profile_is_banned_from_voting_problem_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='community_points',
        ),
        migrations.CreateModel(
            name='ProblemPointsVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.FloatField(help_text='The amount of points you think this problem deserves.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)], verbose_name='points')),
                ('note', models.TextField(help_text='Justification for problem points value.', max_length=2048, verbose_name='note')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem_points_votes', to='judge.Problem')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem_points_votes', to='judge.Profile')),
            ],
        ),
    ]
