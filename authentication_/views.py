from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def lgn(request):

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return render(request, 'authentication_/info.html', context={'info':'Login Feito com sucesso!'})

    return render(request, 'authentication_/login.html')


def lgt(request):
    logout(request)
    return render(request, 'authentication_/info.html', context={'info':'Logout Feito com sucesso!'})
