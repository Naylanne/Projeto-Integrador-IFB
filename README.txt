# Projeto Integrador

Projeto Integrador realizado por:  
**Ester Luiza Souza Campos, Meirejane Figueredo Chaves e Naylanne Lissa Gomes Cunha**  
Curso **Backend - Python com Django** no **IFB/Riacho Fundo**

---

## Descrição do Projeto
O Projeto Integrador consistiu no desenvolvimento de uma API pela empresa **DigitalFlow Solutions** (empresa de tecnologia especializada em plataformas corporativas) 
para o banco de grande porte **InnovaBank**, que precisava de um sistema moderno para gerenciar seu portfólio interno de projetos de TI.

---

## Como Iniciar a API

### 1. Preparar o ambiente
No prompt cmd digite:

python -m venv meuAmbiente

meuAmbiente\Scripts\activate


### 2. Entre na pasta da API utilizando o comando:

cd innova_api


### 3. Instale os frameworks utilizando o seguinte comando:

pip install -r requirements.txt


### 4. Execute as migrações:

python manage.py makemigrations 

python manage.py migrate


### 5. E inicie a API através do comando:

python manage.py runserver

A API abre pelo link: http://127.0.0.1:8000/

---

### A API já conta com um usuário para acesso ao Django administration:

http://127.0.0.1:8000/admin/login/?next=/admin/login

Username: admin
Password: 123456


### 1. Para verificar se já existem usuários: 

python manage.py shell

from django.contrib.auth.models import User
User.objects.all()

<QuerySet []> os usuários aparecem aqui

Sair: exit ()

### 2. Para modificar a senha do usuário:
 
python manage.py changepassword <username>

No caso desse projeto:

python manage.py changepassword admin

Password: <preencha a nova senha>


### 3. Para criar um novo usuário principal:

python manage.py createsuperuser

Username:
Email:
Password:

### 4. Para criar usuários comuns:

python manage.py shell

from django.contrib.auth.models import User
User.objects.create_user(username="joao", password="123456")

---

### Usar token no Swagger com JWT: Bearer SEU_TOKEN_AQUI

---

### Para ter acesso ao visual personalizado da API instale a extensão Live Server no VS Code e abra o arquivo index.html com botão direito/Open with Live Server.

