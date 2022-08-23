from django.db import models

class Department(models.Model):
    '''部门表'''
    title = models.CharField(verbose_name='标题',max_length=32)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    '''员工表'''
    name = models.CharField(verbose_name='姓名',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
    create_time = models.DateField(verbose_name='入职时间')
    depart = models.ForeignKey(verbose_name='部门',to='Department',to_field='id',null=True,blank=True,on_delete=models.SET_NULL)  # 表关联，外表的行被删除时置空
    gender_choices = (
        (1,'男'),
        (2,'女')
    )  # 在django中的约束
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)

class Admin(models.Model):
    '''靓号表'''
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)
