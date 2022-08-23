from django.shortcuts import render, redirect
from django import forms
from management import models


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def login(request):
    '''登录'''
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        admin_object = models.Admin.objects.filter(username=username, password=password).first()
        if admin_object:
            request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
            request.session.set_expiry(60 * 60 * 24 * 7)  # 七天免登录
            return redirect('/user/list')
        form.add_error('username', '用户名或密码错误')
        return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})


def logout(request):
    '''注销'''
    request.session.clear()
    return redirect('/login/')
