# Generated by Django 3.2.8 on 2021-10-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rawmaterial', '0003_auto_20211004_2042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ['name'], 'verbose_name': 'supplier'},
        ),
        migrations.AddField(
            model_name='supplier',
            name='country',
            field=models.CharField(choices=[('FR', 'France'), ('CA', 'Canada'), ('US', 'United States')], default='FR', max_length=2, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='province',
            field=models.CharField(blank=True, choices=[('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NS', 'Nova Scotia'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon')], max_length=2, verbose_name='Province'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='state',
            field=models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, verbose_name='Zip code'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='adress',
            field=models.CharField(blank=True, max_length=200, verbose_name='Adress'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='city',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
