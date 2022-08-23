from django.shortcuts import render, redirect
from django import forms
from management import models


class AdminEditModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ['password']

    def __init__(self, *args, **kwargs):
        super(AdminEditModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def admin_list(request):
    '''管理员列表'''
    queryset = models.Admin.objects.all()
    return render(request, 'admin_list.html', {'queryset': queryset})


def admin_edit(request):
    '''编辑管理员'''
    row_object = models.Admin.objects.all().first()
    if request.method == 'GET':
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'admin_edit.html', {'form': form})

    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'admin_edit.html', {'form': form})
