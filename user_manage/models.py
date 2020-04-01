# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OutCompany(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    company_name = models.CharField(max_length=32)
    company_pri_id = models.BigIntegerField()
    company_identifier = models.CharField(max_length=128)
    note = models.CharField(max_length=64)
    contact = models.CharField(max_length=16)
    contact_phone = models.CharField(max_length=16)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    company_status = models.PositiveIntegerField()
    disable_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'out_company'
        unique_together = (('company_name', 'company_pri_id'),)


class OutCompanyCar(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    out_company_id = models.BigIntegerField()
    vin = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'out_company_car'
        unique_together = (('vin', 'out_company_id'),)


class OutUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    out_company_id = models.BigIntegerField()
    user_name = models.CharField(unique=True, max_length=32)
    password = models.CharField(max_length=128)
    phone = models.CharField(unique=True, max_length=32)
    note = models.CharField(max_length=64)
    user_status = models.PositiveIntegerField()
    disable_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'out_user'


class SysCompany(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_identifier = models.CharField(unique=True, max_length=128)
    create_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    company_name = models.CharField(unique=True, max_length=32)
    alias = models.CharField(max_length=32)
    create_user_id = models.BigIntegerField()
    state = models.PositiveIntegerField()
    contacts = models.CharField(max_length=12)
    contacts_email = models.CharField(max_length=20)
    contacts_phone = models.CharField(max_length=16)
    company_phone = models.CharField(max_length=16)
    company_email = models.CharField(max_length=20)
    company_fax = models.CharField(max_length=16)
    certificates_url = models.CharField(max_length=128)
    additional_url = models.CharField(max_length=128)
    address = models.CharField(max_length=64)
    superior_company_pri_id = models.BigIntegerField()
    logo_url = models.CharField(max_length=128)
    page_url = models.CharField(max_length=128)
    company_type = models.PositiveIntegerField()
    company_describe = models.CharField(max_length=128)
    is_deleted = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'sys_company'


class SysPushKey(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    user_id = models.BigIntegerField()
    push_key = models.CharField(max_length=128)
    push_key_type = models.PositiveIntegerField()
    platform_name = models.CharField(max_length=32)
    system_version = models.CharField(max_length=32)
    app_build = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'sys_push_key'


class SysRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    role_name = models.CharField(max_length=20)
    state = models.PositiveIntegerField()
    note = models.CharField(max_length=64)
    company_pri_id = models.BigIntegerField()
    company_identifier = models.CharField(max_length=128)
    grade = models.PositiveIntegerField()
    is_deleted = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    role_type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'sys_role'
        unique_together = (('role_name', 'company_identifier'),)


class SysRoleParam(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    platform_management_center = models.BigIntegerField()
    business_management = models.BigIntegerField()
    financial_management = models.BigIntegerField()
    report_analysis = models.BigIntegerField()
    user_behavior_analysis = models.BigIntegerField()
    device_management = models.BigIntegerField()
    report_management = models.BigIntegerField()
    system_management = models.BigIntegerField()
    role_id = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'sys_role_param'


class SysUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=32)
    company_pri_id = models.BigIntegerField()
    company_identifier = models.CharField(max_length=128)
    create_user_id = models.BigIntegerField()
    create_user_path = models.CharField(max_length=128)
    user_type = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    alias = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    phone = models.CharField(unique=True, max_length=32)
    state = models.PositiveIntegerField()
    role_id = models.BigIntegerField()
    login_time = models.DateTimeField(blank=True, null=True)
    ip = models.PositiveIntegerField()
    ip_address = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    real_name = models.CharField(max_length=8)
    birthday = models.DateField(blank=True, null=True)
    native_place = models.CharField(max_length=50)
    nation = models.CharField(max_length=10)
    domicile = models.CharField(max_length=50)
    is_deleted = models.PositiveIntegerField()
    sort = models.PositiveIntegerField(default=0)
    note = models.CharField(max_length=64,default='')

    class Meta:
        managed = False
        db_table = 'sys_user'

