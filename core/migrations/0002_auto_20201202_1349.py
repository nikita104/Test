# Generated by Django 3.1.3 on 2020-12-02 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswer',
            name='date_of_passage',
            field=models.DateTimeField(db_index=True, default='2020-02-12', verbose_name='Дата прохождения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='core.teststudent'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_passage', models.DateTimeField(db_index=True, verbose_name='Дата прохождения')),
                ('count_true', models.IntegerField()),
                ('count_false', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teststudent')),
            ],
        ),
    ]