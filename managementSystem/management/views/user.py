from django.shortcuts import render, redirect
from django import forms
from management import models


def user_list(request):
    '''员工管理'''
    queryset = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'queryset': queryset})


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart']

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def user_add(request):
    '''添加员工'''
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})

    # POST提交数据，数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():  # 自动校验
        # 数据合法，保存到数据库
        form.save()
        return redirect('/user/list/')

    # 校验失败
    return render(request, 'user_add.html', {'form': form})


def user_edit(request, nid):
    '''编辑员工'''
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == 'GET':
        # 根据id获取指定行的记录
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():  # 自动校验
        # 数据合法，更新到数据库
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    '''删除员工'''
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
