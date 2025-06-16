# views.py
from django.shortcuts import render

# =============================
#  Vistas públicas / generales
# =============================

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def registro_tipo_usuario(request):
    return render(request, 'registration/seleccion_registro.html')

def registro_cliente(request):
    return render(request, 'registration/registro_cliente.html')

def registro_empresa(request):
    return render(request, 'registration/registro_empresa.html')


# =============================
#  Vistas para CLIENTES
# =============================

def vista_cliente_proyecto(request):
    return render(request, 'cliente/vista_cliente_proyecto.html')

def crear_proyecto_view(request):
    return render(request, 'cliente/crear_proyecto.html')

def publicar_proyecto(request):
    return render(request, 'cliente/publicar_proyecto.html')

def buscar_cliente(request):
    return render(request, 'cliente/buscar.html')

def mis_proyectos_cliente(request):
    return render(request, 'cliente/misproyectos_cli.html')

def ofertas_proyectos(request):
    return render(request, 'cliente/ofertas_proyectos.html')

def mis_propuestas_proyectos(request):
    return render(request, 'cliente/mis_propuestas_proyectos.html')


# =============================
#  Vistas para EMPRESAS
# =============================

def vista_empresa(request):
    return render(request, 'empresa/vista_empresa.html')

def buscar_empresa(request):
    return render(request, 'empresa/buscar.html')

def planes_disponibles(request):
    return render(request, 'empresa/planes_disponibles.html')

def mis_proyectos(request):
    return render(request, 'empresa/mis_proyectos.html')

def dashboard_empresa(request):
    return render(request, 'empresa/dashboard_empresa.html')

def mis_propuestas(request):
    return render(request, 'empresa/mis_propuestas.html')

def formulario_economico(request):
    return render(request, 'empresa/formulario_economico.html')

def formulario_tecnico(request):
    return render(request, 'empresa/formulario_tecnico.html')

def detalle_compra(request):
    return render(request, 'empresa/detalle_compra.html')
