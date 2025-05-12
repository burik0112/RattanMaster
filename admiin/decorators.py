from django.http import HttpResponseForbidden
from functools import wraps

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Вы не авторизованы.")
            if request.user.role not in allowed_roles:
                return HttpResponseForbidden("У вас нет доступа к этой странице.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator