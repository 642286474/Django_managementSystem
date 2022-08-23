# Django_managementSystem
基于Dajngo的简单员工后台管理系统

## 安装依赖库
在终端输入pip download -r requirements.txt -d ./pip_packages

## 数据库迁移
1.首先需要在数据库中手动创建数据库
2.在settings.py中修改数据库连接配置（DATABASES）
3.python manage.py makemigrations
4.python manage.py migrate

## 关于数据
数据需要手动添加

## 模块划分
1、登录模块  management.views.account
2、管理员信息模块  management.views.admin
3、部门模块  management.views.depart
4、员工模块  management.views.user
