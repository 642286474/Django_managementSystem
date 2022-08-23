from django.shortcuts import render, redirect
from management import models


def depart_list(request):
    '''部门列表'''
    # 获取数据库中所有部门列表
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    '''添加部门'''
    if request.method == 'GET':
        return render(request, 'depart_add.html')

    # 获取用户post提交过来的数据
    title = request.POST.get('title')
    # 保存到数据库
    models.Department.objects.create(title=title)
    # 重定向回部门列表
    return redirect('/depart/list/')


def depart_delete(request):
    '''删除部门'''
    # 获取id
    nid = request.GET.get('nid')
    # 删除
    models.Department.objects.filter(id=nid).delete()
    # 重定向回部门列表
    return redirect('/depart/list/')


def depart_edit(request, nid):
    '''编辑部门'''
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'row_object': row_object})

    # 获取用户提交的标题
    title = request.POST.get('title')
    # 根据id找到数据库中的数据并进行更新
    models.Department.objects.filter(id=nid).update(title=title)
    # 重定向回部门列表
    return redirect('/depart/list/')
