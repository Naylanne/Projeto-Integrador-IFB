from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from departamento.views import DepartamentoViewSet
from projeto.views import ProjetoViewSet
from tecnologia.views import TecnologiaViewSet


def home_view(request):
    
    return render(request, 'index.html', {'message': 'Bem-vindo ao Innova API! Acesse /admin para o painel de administração.'})


router = routers.DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'projetos', ProjetoViewSet)
router.register(r'tecnologias', TecnologiaViewSet)


urlpatterns = [
   
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),    
]