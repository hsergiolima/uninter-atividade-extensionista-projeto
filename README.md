# uninter-atividade-extensionista-projeto
Projeto da disciplina "Atividade Extensionista II - Projeto" do curso de ADS da UNINTER.

# ÍNDICE
1. Introdução
2. Principais requisitos
---
# 1. Introdução
Este projeto visa implementar solução via web para gerenciamento de pessoas relacionadas ao Programa de Extensão da UFRPE "Agroflorestando".
Este gerenciamento inclui um sistema web de cadastro com os dados de cada voluntário, o registro de suas atividades desempenhadas no Programa, bem como a quantidade de horas executada em cada atividade.
O sistema fornece o relatório individual ao usuário comum e um relatório geral para usuários com perfis de privilégio.
---
# 2. Principais requisitos
- Desenvolver tela principal estilo 'home page' do projeto
- Na tela principal, apresentar as últimas notícias do projeto
- Na tela principal, dispor espaço de acesso via login para membros e administradores
- Na tela do membro, visualizar opções de: editar perfil, histórico de eventos, saldo de horas, inscrever em eventos abertos
- Na tela de admin, visualizar tabela de membros, ver histórico de membros e seu saldo de horas, gerenciar eventos
---
## 2.1 Home Page
- Título do projeto
- Menu lateral esquerdo com principais rotas para outras páginas
- Menu superior direito para área de acesso do membro e do admin
- Quadro principal com as últimas notícias, em formato de blog
---
## 2.2 Tela do membro
- Na tela principal, apresentar dashboard com informações
    - Últimas eventos inscritos e data de participação
    - Gráfico em pizza com horas realizadas, percentual realizado e percentual restante para completar a carga horária
    - Menu lateral direito com rotas para: editar perfil, histórico completo de eventos, saldo de horas (dashboard principal), eventos abertos
---
## 2.3 Tela de admin
- Na tela principal, apresentar botões com as opções
    - Gerenciar membros
    - Gerenciar eventos
    - Dashboard com números do projeto
