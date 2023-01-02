from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from .models import Classe
from .models import Brand
import random
from .models import Ativo
from pessoal.models import Departamento
from .models import Pacote
from django.contrib.auth.models import User
from pessoal.models import RelColabDpto
from .models import RelacionamentoPacote

lg_url = '/autenticacao/login/'


def id_item(n=6):
    v='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    r=''
    for _ in range(n):
        r+=v[random.randint(0,35)]
    return r


# Create your views here.
@login_required(login_url=lg_url)
def ativos(request):
    return render(request, 'ativos/ativos.html')


@login_required(login_url=lg_url)
def classes(request):
    if request.method == 'POST':
        if request.POST['type'] == 'crt':
            return HttpResponseRedirect('/ativos/classes/criacao/')
        if request.POST['type'] == 'lst':
            return HttpResponseRedirect('/ativos/classes/listagem/')

    return render(request, 'ativos/ativos.html', context={
        'modo':'classes'
    })

@login_required(login_url=lg_url)
def crtcls(request):
    if request.method == 'POST':
        if Classe.objects.filter(name=request.POST['nome-da-classe']):
            return render(request, 'ativos/ativos.html', context={
                'modo':'info',
                'content':'Essa classe ja existe!'
            })
        cls = Classe()
        cls.name = request.POST['nome-da-classe']
        cls.description = request.POST['descricao']
        cls.save()
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Classe criada com sucesso!'
        })

    return render(request, 'ativos/ativos.html', context={
        'modo':'crtcls'
    })


@login_required(login_url=lg_url)
def lstcls(request):
    clss = Classe.objects.all()
    return render(request, 'ativos/ativos.html', context={
        'modo':'lstcls',
        'classes':clss,
    })



@login_required(login_url=lg_url)
def atzcls(request, id):
    try:
        cls = Classe.objects.get(id=id)
    except:
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Essa classe não existe!'
        }) 
    else:
        if request.method == 'POST':
            cls.name = request.POST['nome-da-classe']
            cls.description = request.POST['descricao']
            cls.save()
            return render(request, 'ativos/ativos.html', context={
                'modo':'atzcls',
                'cls':cls,
                'alert':'Classe atualizada com sucesso!',
            })
        return render(request, 'ativos/ativos.html', context={
            'modo':'atzcls',
            'cls':cls,
        })


@login_required(login_url=lg_url)
def delcls(request, id):
    try:
        cls = Classe.objects.get(id=id)
    except:
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Essa marca não existe!'
        })
    else:
        if request.method == 'POST':
            cls.delete()
            return render(request, 'ativos/ativos.html', context={
                'modo':'info',
                'content':'Marca deletada com sucesso!'
            })
        return render(request, 'ativos/ativos.html', context={
            'modo':'delcls',
            'classes':cls,
        })

@login_required(login_url=lg_url)
def brds(request):
    if request.method == 'POST':
        try:
            request.POST['lstbrd']
        except:
            pass
        else:
            return HttpResponseRedirect('/ativos/marcas/listagem/')
        
        try:
            request.POST['crtbrd']
        except:
            pass
        else:
            return HttpResponseRedirect('/ativos/marcas/criacao/')

    return render(request, 'ativos/ativos.html', context={
        'modo':'brds',
    })


@login_required(login_url=lg_url)
def gestao(request):
    if request.method == 'POST':
        try:
            tp = request.POST['type']
        except:
            return render(request, 'ativos/ativos.html', context={
                'modo':'info',
                'content':'Essa opção não existe!'
            })
        else:
            if tp == 'crt':
                return HttpResponseRedirect('/ativos/gestao/criacao/')
            if tp == 'lst':
                return HttpResponseRedirect('/ativos/gestao/listagem/')

    return render(request, 'ativos/ativos.html', context={
        'modo':'gestao',
    })


@login_required(login_url=lg_url)
def crtbrd(request):
    if request.method == 'POST':
        if Brand.objects.filter(brand_name=request.POST['nome-da-marca']):
            return render(request, 'ativos/ativos.html', context={
                'modo':'info',
                'content':'Essa marca ja existe!'
            })
        brd = Brand()
        brd.brand_name = request.POST['nome-da-marca']
        brd.save()
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Marca criada com sucesso!'
        })

    return render(request, 'ativos/ativos.html', context={
        'modo':'crtbrd'
    })


@login_required(login_url=lg_url)
def lstbrd(request):
    brd = Brand.objects.all()
    return render(request, 'ativos/ativos.html', context={
        'modo':'lstbrd',
        'brand':brd,
    })


@login_required(login_url=lg_url)
def atzbrd(request,id):
    try:
        brd = Brand.objects.get(id=id)
    except:
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Essa marca não existe!'
        }) 
    else:
        if request.method == 'POST':
            brd.brand_name = request.POST['nome-da-marca']
            brd.save()
            return render(request, 'ativos/ativos.html', context={
                'modo':'atzbrd',
                'brd':brd,
                'alert':'Marca atualizada com sucesso!',
            })
        return render(request, 'ativos/ativos.html', context={
            'modo':'atzbrd',
            'brand':brd,
        })


@login_required(login_url=lg_url)
def delbrd(request, id):
    try:
        brd = Brand.objects.get(id=id)
    except:
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Essa marca não existe!'
        })
    else:
        if request.method == 'POST':
            brd.delete()
            return render(request, 'ativos/ativos.html', context={
                'modo':'info',
                'content':'Marca deletada com sucesso!'
            })
        return render(request, 'ativos/ativos.html', context={
            'modo':'delbrd',
            'brand':brd,
        })

@login_required(login_url=lg_url)
def crtatv(request):
    if request.method == 'POST':
        ativo = Ativo()
        ativo.id = request.POST['id_atv']
        ativo.item_class = Classe.objects.get(id=request.POST['cls'])
        ativo.brand = Brand.objects.get(id=request.POST['brd'])
        ativo.item_id = request.POST['atv-id']
        ativo.item_model = request.POST['model-atv']
        ativo.especifications = request.POST['espec']
        ativo.status = True
        ativo.save()
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Ativo criado com sucesso!'
        })

    while True:
        id = id_item()
        try:
            Ativo.objects.get(id=id)
        except:
            break
        else:
            continue
    cls = Classe.objects.all()
    brds = Brand.objects.all()
    return render(request, 'ativos/ativos.html', context={
        'modo':'crtatv',
        'id_atv': id,
        'classes':cls,
        'brands':brds
    })

@login_required(login_url=lg_url)
def lstatv(request):
    ativos = Ativo.objects.all()
    brands = Brand.objects.all()
    clss = Classe.objects.all()
    
    if request.method == 'POST':
        if request.POST['item-id']:
            ativos = [a for a in ativos if a.id == request.POST['item-id']]
        if request.POST['classes']:
            try:
                classe = Classe.objects.get(id=request.POST['classes'])
            except:
                classe = []
            else:
                ativos = [a for a in ativos if a.item_class == classe]
        if request.POST['marca']:
            try:
                marca = Brand.objects.get(id=request.POST['marca'])
            except:
                marca = []
            else:
                ativos = [a for a in ativos if a.brand == marca]
        if request.POST['item-model']:
            ativos = [a for a in ativos if a.item_model == request.POST['item-model']]
        if request.POST['status']:
            if request.POST['status'] == 'a':
                s = False
            else:
                s = True
            ativos = [a for a in ativos if a.status == s]
    
    return render(request, 'ativos/ativos.html', context={
        'modo':'lstatv',
        'ativos':ativos,
        'brands':brands,
        'classes':clss,
    })

@login_required(login_url=lg_url)
def atzatv(request, id):
    try:
        ativo = Ativo.objects.get(id=id)
        pkgs = [pkg.pacote for pkg in RelacionamentoPacote.objects.filter(ativo=ativo).order_by('-created_at')]
    except:
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Este ativo não existe!'
        })
    else:
        classes = Classe.objects.all()
        brands = Brand.objects.all()
        if request.method == 'POST':
            if request.POST['cls']:
                ativo.item_class = Classe.objects.get(id=request.POST['cls'])
            if request.POST['brd']:
                ativo.brand = Brand.objects.get(id=request.POST['brd'])
            if request.POST['atv-id']:
                ativo.item_id = request.POST['atv-id']
            if request.POST['model-atv']:
                ativo.item_model = request.POST['model-atv']
            if request.POST['espec']:
                ativo.especifications = request.POST['espec']
        
            ativo.save()
        
        return render(request, 'ativos/ativos.html', context={
            'modo':'atzatv',
            'ativo':ativo,
            'classes':classes,
            'brands':brands,
            'pkgs':pkgs,
        })


@login_required(login_url=lg_url)
def delatv(request, id):
    try:
        atv = Ativo.objects.get(id=id)
    except:
        return render(request, 'ativos/ativos.html', context={
                'modo':'info',
                'content':'Esse ativo não existe!'
            })
    else:
        if request.method == 'POST':
            atv.delete()
            return render(request, 'ativos/ativos.html', context={
                'modo':'info',
                'content':'Ativo deletado com sucesso!'
            })
        return render(request, 'ativos/ativos.html', context={
            'ativo':atv,
            'modo':'delatv',
        })

@login_required(login_url=lg_url)
def pacotes(request):
    if request.method == 'POST':
        if request.POST['type'] == 'crt':
            return HttpResponseRedirect('/ativos/pacotes/criacao/')
        if request.POST['type'] == 'lst':
            return HttpResponseRedirect('/ativos/pacotes/listagem/')

    return render(request, 'ativos/ativos.html', context={
        'modo':'pacotes'
    })


@login_required(login_url=lg_url)
def crtpkg(request):
    if request.method == 'POST':
        try:
            try:
                user = User.objects.get(username=request.POST['colab'])
            except:
                return render(request, 'ativos/ativos.html', context={
                    'modo':'info',
                    'content':'Este usuário não existe!'
                })
            
            dpto = Departamento.objects.get(id=request.POST['dpto'])
            
            if not RelColabDpto.objects.filter(user=user,dpto=dpto):
                return render(request, 'ativos/ativos.html', context={
                    'modo':'info',
                    'content':'Esse usuário pode não pertencer a este departamento!'
                })
            
            pkg = Pacote()
            pkg.id = request.POST['idpkg']
            pkg.type = True if request.POST['pkgtype'] == 'e' else False
            pkg.department = dpto

            pkg.owner = user
            pkg.reason = request.POST['reazon']
            pkg.save()

        except:
            return render(request, 'ativos/ativos.html', context={
                'modo':'info',
                'content':'Ocorreu algum erro, tente novamente!'
            })
        else:
            return render(request, 'ativos/ativos.html', context={
                'modo':'info',
                'content':'Pacote criado com sucesso!'
            })

    while True:
        id = id_item(7)
        try:
            Pacote.objects.get(id=id)
        except:
            break
        else:
            continue

    departamentos = Departamento.objects.all()
    return render(request, 'ativos/ativos.html', context={
        'modo':'crtpkg',
        'id':id,
        'departamentos':departamentos
    })


@login_required(login_url=lg_url)
def lstpkg(request):
    pkgs = Pacote.objects.all().order_by('-updated_at')
    departamentos = Departamento.objects.all()
    if request.method == 'POST':
        if request.POST['pkg-id']:
            pkgs = [pkg for pkg in pkgs if pkg.id==request.POST['pkg-id']]
        if request.POST['movimentacao']:
            type = True if request.POST['movimentacao'] == 'e' else False
            pkgs = [pkg for pkg in pkgs if pkg.type==type]
        if request.POST['status']:
            status = True if request.POST['status'] == 'a' else False
            pkgs = [pkg for pkg in pkgs if pkg.open==status]
        if request.POST['dpto-id']:
            pkgs = [pkg for pkg in pkgs if str(pkg.department.id)==request.POST['dpto-id']]
        if request.POST['item-owner']:
            pkgs = [pkg for pkg in pkgs if pkg.owner.username==request.POST['item-owner']]

    return render(request, 'ativos/ativos.html', context={
        'modo':'lstpkg',
        'pkgs':pkgs,
        'departamentos':departamentos
    })


@login_required(login_url=lg_url)
def atzpkg(request, id):
    try:
        pkg = Pacote.objects.get(id=id)
    except:
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Esse pacote não existe!'
        })
    
    ativos = RelacionamentoPacote.objects.filter(pacote=pkg)

    if request.method == 'POST':
        try:
            try:
                pkg = Pacote.objects.get(id=id)
            except:
                return render(request, 'ativos/ativos.html', context={
                    'modo':'info',
                    'content':'Este pacote não existe!'
                })
            
            pkg.type = True if request.POST['pkgtype'] == 'e' else False
            pkg.reason = request.POST['reazon']
            pkg.save()

        except:
            return render(request, 'ativos/ativos.html', context={
                'modo':'info',
                'content':'Ocorreu algum erro, tente novamente!'
            })
        else:
            return render(request, 'ativos/ativos.html', context={
                'modo':'atzpkg',
                'pkg':pkg,
                'ativos':ativos,
                'alert':'Pacote atualizado com sucesso!',
            })


    return render(request, 'ativos/ativos.html', context={
        'modo':'atzpkg',
        'pkg':pkg,
        'ativos':ativos,
    })


@login_required(login_url=lg_url)
def mngpkg(request, id):
    try:
        pkg = Pacote.objects.get(id=id)
    except:
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Esse pacote não existe!'
        })

    rel = RelacionamentoPacote.objects.filter(pacote=pkg)

    em_pkg = [relacionamento.ativo for relacionamento in rel]
    
    ativos = Ativo.objects.filter(status=not pkg.type)
    classes = Classe.objects.all()
    marcas = Brand.objects.all()

    if request.method == 'POST':
        if request.POST['modo'] == 'filter':
            if request.POST['incluso']:
                if request.POST['incluso'] == 's':
                    ativos = em_pkg
                else:
                    ativos = [ativo for ativo in ativos if ativo not in em_pkg]
            if request.POST['modo'] == 'filter':
                if request.POST['item-id']:
                    ativos = [a for a in ativos if a.id == request.POST['item-id']]
                if request.POST['classes']:
                    try:
                        classe = Classe.objects.get(id=request.POST['classes'])
                    except:
                        classe = []
                    else:
                        ativos = [a for a in ativos if a.item_class == classe]
                if request.POST['marca']:
                    try:
                        marca = Brand.objects.get(id=request.POST['marca'])
                    except:
                        marca = []
                    else:
                        ativos = [a for a in ativos if a.brand == marca]
                if request.POST['item-model']:
                    ativos = [a for a in ativos if a.item_model == request.POST['item-model']]

        if request.POST['modo'] == 'atz':

            for ativo in em_pkg:
                ativo.status = not pkg.type
                ativo.save()

            rel.delete()
            em_pkg = []
                
            for item in request.POST.getlist('pkg-item'):
                try:
                    rel = RelacionamentoPacote()
                    ativo = Ativo.objects.get(id=item)
                    ativo.status = pkg.type
                    rel.pacote = pkg
                    rel.ativo = ativo
                except Exception as e:
                    print(e)
                    return render(request, 'ativos/ativos.html', context={
                        'alert':'Algo deu errado, tente novamente!',
                        'modo':'mngpkg',
                        'ativos':ativos,
                        'pkg':pkg,
                        'classes':classes,
                        'brands':marcas,
                    })
                else:
                    ativo.save()
                    rel.save()

            return  HttpResponseRedirect(f'/ativos/pacote/{pkg.id}/')

    return render(request, 'ativos/ativos.html', context={
        'modo':'mngpkg',
        'ativos':ativos,
        'pkg':pkg,
        'classes':classes,
        'brands':marcas,
        'em_pkg':em_pkg,
    })


@login_required(login_url=lg_url)
def delpkg(request, id):
    try:
        pkg = Pacote.objects.get(id=id)
    except:
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Esse pacote não existe!'
        })
    
    if RelacionamentoPacote.objects.filter(pacote=pkg):
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Não é possivel excluir um pacote que contenha itens ou que ja tenha sido fechado!'
        })

    if request.method == 'POST':
        pkg.delete()
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Pacote deletado com sucesso!!'
        })


    return render(request, 'ativos/ativos.html', context={
        'modo':'delpkg',
        'pkg':pkg,
    })


@login_required(login_url=lg_url)
def clspkg(request,id):
    try:
        pkg = Pacote.objects.get(id=id)
    except:
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'Esse pacote não existe!'
        })


    if request.method == 'POST':
        pkg.open = False
        pkg.save()
        return render(request, 'ativos/ativos.html', context={
            'modo':'info',
            'content':'O pacote foi encerrado com sucesso!'
        })
    
    return render(request, 'ativos/ativos.html', context={
        'modo':'clspkg',
        'pkg':pkg,
    })