from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class M1(MiddlewareMixin):
    def process_request(self, request):
        # 获取用户session信息
        if request.path_info == '/login/':
            return
        info_dict = request.session.get('info')
        if info_dict:
            return

        return redirect('/login/')
