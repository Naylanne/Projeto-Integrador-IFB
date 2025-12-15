import os
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation
from django.conf import settings
from django.core.management.base import BaseCommand
from departamento.models import Departamento
from tecnologia.models import Tecnologia
from projeto.models import Projeto


CSV_DIR = os.path.join(settings.BASE_DIR, 'dados')
CSV_DELIMITER = ','
DATE_FORMATS = ['%Y-%m-%d', '%d/%m/%Y', '%Y/%m/%d']

def parse_date(date_str):
    if not date_str:
        return None

    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue

    raise ValueError(f"Formato de data inválido: {date_str}")

def parse_decimal(decimal_str):
    if not decimal_str:
        return None

    try:
        cleaned_str = (
            decimal_str.replace('R$', '')
            .replace('.', '')
            .replace(',', '.')
            .strip()
        )

        if not cleaned_str:
            return None

        return Decimal(cleaned_str)

    except InvalidOperation:
        raise ValueError(f"Formato de número decimal inválido: {decimal_str}")

class Command(BaseCommand):
    help = 'Importa dados de Departamento, Tecnologia e Projeto a partir de arquivos CSV.'

    def add_arguments(self, parser):
        parser.add_argument(
            'tipo',
            nargs='?',
            choices=['departamento', 'tecnologia', 'projeto', 'todos'],
            default='todos',
            help='Define qual CSV será importado'
        )

    def handle(self, *args, **options):
        tipo = options['tipo']

        self.stdout.write(self.style.NOTICE('--- Iniciando a importação de dados ---'))
        self.stdout.write(f'Diretório CSV: {CSV_DIR}')

        sucesso = 0
        falhas = 0

        if tipo in ['departamento', 'todos']:
            if self.importar_departamentos():
                sucesso += 1
            else:
                falhas += 1

        if tipo in ['tecnologia', 'todos']:
            if self.importar_tecnologias():
                sucesso += 1
            else:
                falhas += 1

        if tipo in ['projeto', 'todos']:
            if self.importar_projetos():
                sucesso += 1
            else:
                falhas += 1

        if sucesso > 0 and falhas == 0:
            self.stdout.write(
                self.style.SUCCESS('--- Importação concluída com sucesso! ---')
            )
        elif sucesso > 0 and falhas > 0:
            self.stdout.write(
                self.style.WARNING(
                    '--- Importação finalizada com avisos. Alguns dados podem não ter sido importados ---'
                )
            )
        else:
            self.stdout.write(
                self.style.ERROR(
                    '--- Importação finalizada com falhas. Nenhum dado foi importado. ---'
                )
            )
    
    def importar_departamentos(self):
        filename = os.path.join(CSV_DIR, 'departamentos.csv')
        self.stdout.write(f'Importando Departamentos de {filename}...')

        if not os.path.exists(filename):
            self.stdout.write(self.style.ERROR(f"Arquivo '{filename}' não encontrado."))
            return False

        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=CSV_DELIMITER)
                count = 0

                for row in reader:
                    nome = row.get('nome', '').strip()
                    if not nome:
                        continue

                    ativo_val = row.get('ativo', '').strip().lower() in ['true', '1', 'sim']

                    Departamento.objects.update_or_create(
                        nome=nome,
                        defaults={
                            'gestor': row.get('gestor', '').strip(),
                            'descricao': row.get('descricao', '').strip(),
                            'ativo': ativo_val,
                        }
                    )
                    count += 1

                self.stdout.write(
                    self.style.SUCCESS(f'{count} Departamentos importados/atualizados.')
                )
                return True

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar Departamentos: {e}'))
            return False

    def importar_tecnologias(self):
        filename = os.path.join(CSV_DIR, 'tecnologias.csv')
        self.stdout.write(f'Importando Tecnologias de {filename}...')

        if not os.path.exists(filename):
            self.stdout.write(self.style.ERROR(f"Arquivo '{filename}' não encontrado."))
            return False

        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=CSV_DELIMITER)
                count = 0

                for row in reader:
                    nome = row.get('nome', '').strip()
                    if not nome:
                        continue

                    Tecnologia.objects.update_or_create(
                        nome=nome,
                        defaults={
                            'tipo': row.get('tipo', 'Outro').strip(),
                            'versao': row.get('versao', '').strip() or None,
                            'fornecedor': row.get('fornecedor', '').strip(),
                            'descricao': row.get('descricao', '').strip(),
                        }
                    )
                    count += 1

                self.stdout.write(
                    self.style.SUCCESS(f'{count} Tecnologias importadas/atualizadas.')
                )
                return True

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar Tecnologias: {e}'))
            return False

    def importar_projetos(self):
        filename = os.path.join(CSV_DIR, 'projetos.csv')
        self.stdout.write(f'Importando Projetos de {filename}...')

        if not os.path.exists(filename):
            self.stdout.write(self.style.ERROR(f"Arquivo '{filename}' não encontrado."))
            return False

        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=CSV_DELIMITER)
                count = 0

                for row in reader:
                    nome = row.get('nome', '').strip()
                    if not nome:
                        continue

                    departamento_nome = row.get('departamento_nome', '').strip()
                    if not departamento_nome:
                        self.stdout.write(
                            self.style.ERROR(f"Projeto '{nome}' sem departamento_nome.")
                        )
                        continue

                    try:
                        departamento = Departamento.objects.get(nome=departamento_nome)
                    except Departamento.DoesNotExist:
                        self.stdout.write(
                            self.style.ERROR(f"Departamento '{departamento_nome}' não encontrado.")
                        )
                        continue

                    data_inicio = parse_date(row.get('data_inicio', '').strip())
                    data_fim = parse_date(row.get('data_fim', '').strip())
                    orcamento = parse_decimal(row.get('orcamento', '').strip())

                    projeto, _ = Projeto.objects.update_or_create(
                        nome=nome,
                        defaults={
                            'descricao': row.get('descricao', '').strip(),
                            'departamento': departamento,
                            'data_inicio': data_inicio,
                            'data_fim': data_fim,
                            'status': row.get('status', 'Planejado').strip(),
                            'risco': row.get('risco', 'Baixo').strip(),
                            'orcamento': orcamento,
                        }
                    )

                    tecnologias_str = row.get('tecnologias_nomes', '').strip()
                    tecnologias_nomes = [
                        t.strip() for t in tecnologias_str.split(';') if t.strip()
                    ]

                    if tecnologias_nomes:
                        tecnologias_objs = Tecnologia.objects.filter(
                            nome__in=tecnologias_nomes
                        )
                        projeto.tecnologias.set(tecnologias_objs)
                    else:
                        projeto.tecnologias.clear()

                    count += 1

                self.stdout.write(
                    self.style.SUCCESS(f'{count} Projetos importados/atualizados.')
                )
                return True

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar Projetos: {e}'))
            return False