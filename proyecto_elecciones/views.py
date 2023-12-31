from django.shortcuts import redirect, render
from app1.models import Usuario, Candidato, Voto, Lista

def home(request):    
    data={}
    votos = Voto.objects.all()
    data["votos"] = votos
    return render(request, "home.html",data)

def login(request):
    data={}
    candidatos = Candidato.objects.all()
    data["candidatos"]=candidatos
    cedula_ingresada = request.POST.get("txtCedula")    
    try:
        usuario = Usuario.objects.get(cedula=cedula_ingresada)
        data["usuario"] = usuario
        return render(request, 'eleccion.html', data)
    except Usuario.DoesNotExist:        
        return redirect("home")
    
def confirmarVoto(request,id, cedula):
    candidato = Candidato.objects.get(pk=id)
    usuario = Usuario.objects.get(pk=cedula)    
    voto = Voto(
        nombre_candidato = candidato,
        cedula_votante = usuario
    )
    voto.save()
    return redirect("home")
