"""ChileProyectos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    # ============================
    #  Admin & Autenticación
    # ============================
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # ============================
    #  Vistas públicas / Registro
    # ============================
    path('', views.home, name='home'),  # Página de inicio
    path('registro/', views.registro_tipo_usuario, name='seleccion_registro'),  # Selección Cliente / Empresa
    path('registro/cliente/', views.registro_cliente, name='registro_cliente'),
    path('registro/empresa/', views.registro_empresa, name='registro_empresa'),

    # ============================
    #  Rutas para CLIENTES
    # ============================
    path('vista_cliente_proyecto/', views.vista_cliente_proyecto, name='vista_cliente_proyecto'),  # Vista principal de cliente
    path('crear-proyecto/', views.crear_proyecto_view, name='crear_proyecto'),  # Formulario creación
    path('publicar-proyecto/', views.publicar_proyecto, name='publicar_proyecto'),  # Paso final publicación
    path('mis_proyectos_cliente/', views.mis_proyectos_cliente, name='mis_proyectos_cliente'),  # Lista de proyectos creados
    path('ofertas_proyectos/', views.ofertas_proyectos, name='ofertas_proyectos'),  # Ver ofertas recibidas
    path('mis_propuetas_proyectos/', views.mis_propuestas_proyectos, name='mis_propuestas_proyectos'),  # Postulaciones recibidas
    path('buscar/cliente/', views.buscar_cliente, name='buscar_cliente'),  # Buscador empresa
   
    # ============================
    #  Rutas para EMPRESAS
    # ============================
    path('vista-empresa/', views.vista_empresa, name='vista_empresa'),  # Vista principal para empresa
    path('buscar/empresa/', views.buscar_empresa, name='buscar_empresa'),  # Buscador empresa
    path('planes/', views.planes_disponibles, name='planes_disponibles'),  # Página de planes
    path('mis-proyectos/', views.mis_proyectos, name='mis_proyectos'),  # Proyectos comprados
    path('dashboard-empresa/', views.dashboard_empresa, name='dashboard_empresa'),  # Dashboard empresa
    path('mis_propuestas/', views.mis_propuestas, name='mis_propuestas'),  # Proyectos donde postuló

    # Formularios para enviar propuestas
    path('formulario_economico/', views.formulario_economico, name='formulario_economico'),
    path('formulario_tecnico/', views.formulario_tecnico, name='formulario_tecnico'),

    # Vista de detalle de compra de contacto
    path('detalle_compra/', views.detalle_compra, name='detalle_compra'),
]