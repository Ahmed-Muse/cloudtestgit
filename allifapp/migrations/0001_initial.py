# Generated by Django 5.0.2 on 2024-04-20 07:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SectorsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('notes', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('pobox', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('website', models.CharField(blank=True, max_length=50, null=True)),
                ('phone1', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('phone2', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='secrlmcomp', to='allifapp.sectorsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, choices=[('Somalia', 'Somalia'), ('Kenya', 'Kenya'), ('Other', 'Other')], max_length=30)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('sales', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('balance', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('turnover', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('contact', models.CharField(blank=True, max_length=30, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cuscmprln', to='allifapp.companydetailsmodel')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cuscmprlne', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffNo', models.IntegerField(default='0', unique=True)),
                ('firstName', models.CharField(max_length=50, null=True)),
                ('lastName', models.CharField(max_length=50, null=True)),
                ('middleName', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=25, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('education', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.CharField(blank=True, max_length=50, null=True)),
                ('dateJoined', models.DateTimeField(auto_now_add=True, null=True)),
                ('salary', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('total_salary_paid', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10, null=True)),
                ('salary_payable', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('salary_balance', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('sysperms', models.CharField(blank=True, choices=[('admin', 'admin'), ('staff', 'staff'), ('owner', 'owner'), ('guest', 'guest'), ('manager', 'manager'), ('director', 'director')], default='staff', max_length=30, null=True)),
                ('stffslug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emplcomprlnmefsa', to='allifapp.companydetailsmodel')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allifquoteitemrelatedfgfd', to='allifapp.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuotesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cuscmprlqtn', to='allifapp.companydetailsmodel')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apqotelnm', to='allifapp.customersmodel')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cuscmprlneqt', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteItemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('quoteconn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allifquoteitemrelated', to='allifapp.quotesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='SuppliersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, choices=[('Somalia', 'Somalia'), ('Kenya', 'Kenya'), ('Other', 'Other')], max_length=30)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('balance', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('turnover', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('contact', models.CharField(blank=True, max_length=30, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('company', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='cmpsuprlnmes', to='allifapp.companydetailsmodel')),
            ],
        ),
    ]