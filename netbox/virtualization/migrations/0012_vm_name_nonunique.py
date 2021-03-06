# Generated by Django 2.2.6 on 2019-12-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0006_custom_tag_models'),
        ('virtualization', '0011_3569_virtualmachine_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualmachine',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='virtualmachine',
            unique_together={('cluster', 'tenant', 'name')},
        ),
    ]
