# Generated by Django 4.0.5 on 2022-06-13 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_send_message_advuser_send_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Название')),
                ('order', models.SmallIntegerField(db_index=True, default=0, verbose_name='Порядок')),
            ],
        ),
        migrations.CreateModel(
            name='SubRubric',
            fields=[
                ('rubric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.rubric')),
            ],
            bases=('main.rubric',),
        ),
        migrations.CreateModel(
            name='SuperRubric',
            fields=[
            ],
            options={
                'verbose_name': 'Надрубрика',
                'verbose_name_plural': 'Надрубрики',
                'ordering': ('order', 'name'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.rubric',),
        ),
        migrations.AddField(
            model_name='rubric',
            name='super_rubric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.superrubric', verbose_name='Надрубрика'),
        ),
    ]