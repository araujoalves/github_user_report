# github_user_report


Resumo do Código
Este projeto em Python permite obter informações detalhadas sobre um usuário do GitHub, utilizando a API do GitHub. A seguir está um resumo das funcionalidades e componentes principais do código:

Funcionalidades
Obtenção de Dados do Usuário:

A função get_user faz uma requisição à API do GitHub para obter informações de um usuário específico, como nome de usuário, URL do perfil, número de repositórios públicos, número de seguidores e número de usuários que o usuário segue. Os dados são armazenados em um objeto da classe User.
Obtenção de Repositórios do Usuário:

A função get_user_repos faz uma requisição à API do GitHub para obter a lista de repositórios públicos de um usuário específico. Retorna um dicionário onde a chave é o nome do repositório e o valor é a URL do repositório.
Geração de Relatório:

A função user_report gera um relatório em formato de texto com as informações do usuário e seus repositórios. O relatório é salvo em um arquivo nomeado com o login do usuário e também é impresso no console.
Testes Unitários:

A classe TestMethods utiliza o módulo unittest para realizar testes unitários que verificam se a classe User tem os atributos necessários e se a função get_user_repos retorna um dicionário válido.
Componentes Principais
Classe User: Representa um usuário do GitHub com atributos como login, nome, URL do perfil, número de repositórios públicos, número de seguidores e número de usuários seguidos.

Funções:

get_user: Faz uma requisição à API do GitHub para obter os dados de um usuário e retorna um objeto User.
get_user_repos: Faz uma requisição à API do GitHub para obter os repositórios públicos de um usuário e retorna um dicionário com os nomes e URLs dos repositórios.
user_report: Gera um relatório com os dados do usuário e seus repositórios, salvando-o em um arquivo de texto e imprimindo-o no console.
Testes Unitários:

test_user_class_has_minimal_parameters: Verifica se a classe User tem os atributos mínimos necessários.
test_get_user_repos: Verifica se a função get_user_repos retorna um dicionário válido com nomes e URLs de repositórios.
Execução
Ao executar o script principal:

Define-se o nome de usuário do GitHub a ser usado.
Obtêm-se os dados do usuário e seus repositórios.
Gera-se o relatório e imprime-se no console.
Executam-se os testes unitários para garantir a funcionalidade correta.
Este projeto é útil para obter e relatar informações básicas de usuários do GitHub de forma automatizada e verificável.
