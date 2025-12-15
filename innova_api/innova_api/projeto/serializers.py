from rest_framework import serializers
from .models import Projeto
from tecnologia.models import Tecnologia
from tecnologia.serializers import TecnologiaSerializer


class ProjetoSerializer(serializers.ModelSerializer):

    tecnologias = TecnologiaSerializer(many=True, read_only=True)

    tecnologias_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tecnologia.objects.all(),
        many=True,
        write_only=True,
        source='tecnologias'
    )

    class Meta:
        model = Projeto
        fields = [
            'id',
            'nome',
            'descricao',
            'departamento',
            'data_inicio',
            'data_fim',
            'status',
            'risco',
            'orcamento',
            'tecnologias',
            'tecnologias_ids'
        ]

        read_only_fields = ['tecnologias']