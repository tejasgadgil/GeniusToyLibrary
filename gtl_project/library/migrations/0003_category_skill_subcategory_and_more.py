# Generated by Django 4.2.2 on 2024-02-26 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='prod_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prodType',
            new_name='prod_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='maxAge',
        ),
        migrations.RemoveField(
            model_name='product',
            name='minAge',
        ),
        migrations.AddField(
            model_name='product',
            name='age_from',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='age_to',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='for_disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='no_of_pieces',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='skills',
            field=models.ManyToManyField(to='library.skill'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.subcategory'),
        ),
    ]
