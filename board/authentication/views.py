from django.shortcuts import render, redirect,HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.decorators import login_required

@login_required
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('admin:index')

    return render(request, 'authentication/home.html')

@login_required
@require_http_methods(['GET'])
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('https://api.tu.ac.th/logout/?next={}'.format(request.META['HTTP_REFERER']))