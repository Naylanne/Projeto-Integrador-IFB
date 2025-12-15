from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from .models import Tecnologia
from .serializers import TecnologiaSerializer


class TecnologiaFilter(FilterSet):
    tipo = CharFilter(field_name="tipo", lookup_expr="iexact")

    class Meta:
        model = Tecnologia
        fields = ['tipo']


class TecnologiaViewSet(viewsets.ModelViewSet):
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = TecnologiaFilter