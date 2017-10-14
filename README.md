# Desenvolvimento Web II - Projeto de Sufiência 

Servidor Web: [Ocorrência](http://lopes.pythonanywhere.com/)


# Instalação:
	$ git clone https://lopeslarissa@bitbucket.org/lopeslarissa/ocorrencia.git
	$ pip install -r requirements.txt
	$ python manage.py make migrations
	$ python manage.py make migrate
	$ python manapy.py populate_db_ocorrencia (opcional)
	$ python manage.py compilemessages 
	
# Documentação:
	$ cd sistema/docs
	$ make html
- Acesse o diretório sistena/docs/_build/html/
- Abra o documento index.html com seu navegador
	
## Requisitos do Projeto

# Desenvolver um projeto da seguinte forma:
- Desenvolver utilizando um dos frameworks web Python: Django ou Flask
- Modelo ER 
- Modelo de Classes
- Ser desenvolvido utilizando GIT durante todo o processo, com commits a cada etapa 
- Ser feita a publicação em um servidor e passar a URL para acesso
- De 2 a 4 entidades (tabelas)
- Autenticação de usuários com pelo menos acessos diferenciados para usuários autenticados e visitantes
- CSS (bootstrap ou semelhantes) 

# Serão verificados:
- Utilização de virtualenv, com arquivo requirements.txt
- Estrutura e organização do projeto em pastas e arquivos (Models, Forms, Views e Admin em arquivos separados)
- Uso de herança de templates (base.html)
- Pelo menos um uso de Class Based Views (CBV) e um de Generic Class Based View
- Fazer a Localização (tradução para outros idiomas) da aplicação
- Criar a documentação da aplicação com Sphinx (ou semelhante)
- Utilizar Testes de Unidade na aplicação
- Padronização PEP8
- Melhores práticas de desenvolvimento Django

# Observações:
- Enviar convite para que eu participe do projeto e acompanhe o desenvolvimento

# Prazo final para apresentação: 10/11/2017


Projeto avaliativo para fins estritamente acadêmicos.

