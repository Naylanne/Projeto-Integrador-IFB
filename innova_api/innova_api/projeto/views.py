from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateFilter, NumberFilter, CharFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Projeto
from .serializers import ProjetoSerializer


class ProjetoFilter(FilterSet):
    departamento = NumberFilter(field_name="departamento__id", lookup_expr="exact")
    risco = CharFilter(field_name="risco", lookup_expr="exact")
    data_inicio_min = DateFilter(field_name="data_inicio", lookup_expr="gte")
    data_inicio_max = DateFilter(field_name="data_inicio", lookup_expr="lte")
    tecnologia = NumberFilter(field_name="tecnologias__id", lookup_expr="exact")

    class Meta:
        model = Projeto
        fields = ['departamento', 'status', 'risco', 'tecnologia']


class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all().distinct()
    serializer_class = ProjetoSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    search_fields = ['nome', 'descricao']

    ordering_fields = ['data_inicio', 'status', 'risco']

    filterset_class = ProjetoFilter
