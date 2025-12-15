from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, BooleanFilter
from .models import Departamento
from .serializers import DepartamentoSerializer


class DepartamentoFilter(FilterSet):
    ativo = BooleanFilter(field_name="ativo")

    class Meta:
        model = Departamento
        fields = ['ativo']


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = DepartamentoFilter