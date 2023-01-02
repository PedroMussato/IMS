from django.shortcuts import render
from .models import Departamento
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import RelColabDpto


lg_url = '/autenticacao/login/'

# Create your views here.
@login_required(login_url=lg_url)
def pessoal(request):
    return render(request, 'pessoal/pessoal.html')

@login_required(login_url=lg_url)
def departamentos(request):
    departamentos = Departamento.objects.filter()
    return render(request, 'pessoal/pessoal.html', context={
        'modo':'deplst',
        'departamentos':departamentos,
    })

@login_required(login_url=lg_url)
def crt_dep(request):
    if request.method == 'POST':
        try:
            Departamento.objects.get(name=request.POST['nome-do-departamento'])
        except:
            departamento = Departamento()
            departamento.name = str(request.POST['nome-do-departamento'])
            departamento.save()
            return HttpResponseRedirect('/pessoal/departamentos/')
        else:
            return render(request, 'pessoal/pessoal.html', context={
                'modo':'info',
                'content':'Este departamento ja existe!'
            })

    return render(request, 'pessoal/pessoal.html', context={
        'modo':'depcrt',
    })


@login_required(login_url=lg_url)
def departamento(request, id):
    try:
        departamento = Departamento.objects.get(id=id)
    except:
        return render(request, 'pessoal/pessoal.html', context={
            'modo':'info',
            'content':'Este departamento NÃO existe!'
        })
    else:
        if request.method == 'POST':
            departamento.name = request.POST['nome-do-departamento']
            departamento.save()
            return render(request, 'pessoal/pessoal.html', context={
                'modo':'depunico',
                'departamento':departamento,
                'alert':'Departamento atualizado com sucesso!',
            })
        return render(request, 'pessoal/pessoal.html', context={
            'modo':'depunico',
            'departamento':departamento,
        })


@login_required(login_url=lg_url)
def delete_dpto(request,id):
    try:
        departamento = Departamento.objects.get(id=id)
    except:
        return render(request, 'pessoal/pessoal.html', context={
            'modo':'info',
            'content':'Este departamento NÃO existe!'
            })
    else:    
        if request.method == 'POST':
            departamento.delete()
            return render(request, 'pessoal/pessoal.html', context={
            'modo':'info',
            'content':'O departamento foi deletado com sucesso!'
            })
        else:
            return render(request, 'pessoal/pessoal.html', context={
                'modo':'deldep',
                'departamento':departamento
            })


@login_required(login_url=lg_url)
def colaboradores_(request):
    colaboradores = User.objects.filter()
    return render(request, 'pessoal/pessoal.html', context={
    'modo':'colab',
    'colaboradores':colaboradores
    })


@login_required(login_url=lg_url)
def crtcolab(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.is_active = False
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponseRedirect('/pessoal/colaboradores/')

    return render(request, 'pessoal/pessoal.html', context={
    'modo':'crtcolab',
    })


@login_required(login_url=lg_url)
def atzcolab(request, id):
    try:
        colab = User.objects.get(id=id)
    except:
        return render(request, 'pessoal/pessoal.html', context={
            'modo':'info',
            'content':'Este colaborador não existe!'
        })
    else:
        if request.method == 'POST':
            colab.username = request.POST['username']
            colab.email = request.POST['email']
            try:
                request.POST['administrador']
            except:
                colab.is_active = False
            else:
                colab.is_active = True
            
            
            if request.POST['password']:
                colab.set_password(request.POST['password'])
            
            colab.save()


            return render(request, 'pessoal/pessoal.html', context={
            'modo':'atzcolab',
            'colab':colab,
            'alert':'Informações do Colaborador Atualizadas.',
        })

        return render(request, 'pessoal/pessoal.html', context={
            'modo':'atzcolab',
            'colab':colab,
        })

@login_required(login_url=lg_url)
def delcolab(request, id):
    try:
        colaborador = User.objects.get(id=id)
    except:
        return render(request, 'pessoal/pessoal.html', context={
            'modo':'info',
            'content':'Este colaborador NÃO existe!'
            })
    else:
        if request.user.id == colaborador.id:
           return render(request, 'pessoal/pessoal.html', context={
            'modo':'info',
            'content':'Você não pode excluir você mesmo.'
            }) 
        if request.method == 'POST':
            colaborador.delete()
            return render(request, 'pessoal/pessoal.html', context={
            'modo':'info',
            'content':'O colaborador foi deletado com sucesso!'
            })
        else:
            return render(request, 'pessoal/pessoal.html', context={
                'modo':'delcolab',
                'colaborador':colaborador,
            })


@login_required(login_url=lg_url)
def relcols(request):
    if request.method == 'POST':
        try:
            request.POST['crtrel']
            return HttpResponseRedirect('/pessoal/relacionamentos/criacao/')
        except:
            pass
        try:
            request.POST['lstrel']
            return HttpResponseRedirect('/pessoal/relacionamentos/listagem/')
        except:
            pass
        try:
            request.POST['delrel']
            return HttpResponseRedirect('/pessoal/relacionamentos/delecao/')
        except:
            pass

    return render(request, 'pessoal/pessoal.html', context={
        'modo':'relcols',
    })


@login_required(login_url=lg_url)
def crtrelcols(request):
    if request.method == 'POST':
        dpto = Departamento.objects.get(id=request.POST['departamento'])
        try:
            user = User.objects.get(username=request.POST['username'])
        except:
            return render(request, 'pessoal/pessoal.html', context={
                'modo':'info',
                'content':'Este usuário não existe!'
            })
        else:
            if RelColabDpto.objects.filter(user=user,dpto=dpto):
                return render(request, 'pessoal/pessoal.html', context={
                    'modo':'info',
                    'content':'Este relacionamento ja foi criado!'
                }) 
            else:
                relacionamento = RelColabDpto()
                relacionamento.user = user
                relacionamento.dpto = dpto
                relacionamento.save()
                return render(request, 'pessoal/pessoal.html', context={
                    'modo':'info',
                    'content':'Relacionamento criado com sucesso!'
                }) 

    dptos = Departamento.objects.all()
    return render(request, 'pessoal/pessoal.html', context={
        'modo':'crtrelcols',
        'dptos':dptos,
    })


@login_required(login_url=lg_url)
def lstrelcols(request):
    if request.method == 'POST':
        listagem = RelColabDpto.objects.filter(dpto=request.POST['departamento'])

        return render(request, 'pessoal/pessoal.html', context={
            'modo':'lstrelcols',
            'listagem':listagem,
        })
        
    dptos = Departamento.objects.all()
    return render(request, 'pessoal/pessoal.html', context={
        'modo':'flstrelcols',
        'dptos':dptos,
    })


@login_required(login_url=lg_url)
def delrelcols(request, id):
    try:
        rel = RelColabDpto.objects.get(id=id)
    except:
        return render(request, 'pessoal/pessoal.html', context={
            'modo':'info',
            'content':'Este relacionamento não existe!'
        })
    
    if request.method == 'POST':
        rel.delete()
        return render(request, 'pessoal/pessoal.html', context={
            'modo':'info',
            'content':'O relacionamento foi deletado com sucesso!'
        })

    return render(request, 'pessoal/pessoal.html', context={
        'modo':'delrelcols',
        'rel':rel,
    })
