def check_permission(request):
    return request.user.is_staff or request.user.is_superuser or (hasattr(request.user, 'profile') and request.user.profile.is_staff)