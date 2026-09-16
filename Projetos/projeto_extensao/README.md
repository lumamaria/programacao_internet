# Projeto Extensão

## Atividade Prática de Laboratório: Relacionamentos em Django

### Sistema de Gestão de Projetos de Extensão (ProjetoIF)

Nível: 4º Ano - Curso Técnico Integrado

Disciplina: Programação para Internet

## 1. Contexto do Desafio

Vocês foram convocados pela coordenação de extensão do IFRN para iniciar o desenvolvimento do núcleo de banco de dados do novo sistema ProjetoIF. O objetivo desta atividade laboratorial é mapear as entidades e seus relacionamentos no framework Django, validá-los no Django Admin e, por fim, exibi-los em telas para os visitantes do portal acadêmico.

## 2. Modelagem de Dados

No arquivo `models.py` do seu aplicativo, implemente as classes abaixo garantindo os relacionamentos corretos. Lembre-se de importar os tipos de campos adequados e implementar o método `__str__(self)` para cada modelo.

| Modelo | Campos Simples | Relacionamentos |
| --- | --- | --- |
| Categoria | nome (CharField) | - |
| Aluno | nome (CharField), matricula (CharField) | - |
| PerfilAcademico | link_lattes (URLField), biografia (TextField) | aluno (OneToOneField ligado ao modelo Aluno) |
| Projeto | titulo (CharField), descricao (TextField), data_inicio (DateField) | categoria (ForeignKey ligado ao modelo Categoria), equipe (ManyToManyField ligado ao modelo Aluno) |

## 3. O Poder do Admin

Antes de construir as telas, precisamos refletir as mudanças no banco de dados, povoá-lo e garantir que os relacionamentos estão funcionando perfeitamente pela interface administrativa.

1. Abra o terminal e execute os comandos de migração:
2. Crie um superusuário para acessar o painel:
3. Abra o arquivo `admin.py` e registre os 4 modelos criados.
4. Inicie o servidor de desenvolvimento, acesse `/admin` e cadastre:

- 2 Categorias diferentes.
- 3 Alunos (e crie um Perfil Acadêmico para cada um deles).
- 2 Projetos (escolha a categoria e adicione múltiplos alunos na equipe).

## 4. Exibição na Tela

Agora vamos conectar o banco de dados à interface do usuário. Crie as views, as rotas e os templates (HTML) para as duas telas abaixo:

- **Tela de Listagem de Projetos**: Crie uma view que busque todos os projetos e os envie para o template. Na tela, exiba uma lista ou tabela contendo o Título e a Categoria de cada projeto.
- **Tela de Detalhes do Projeto**: Crie uma view que busque apenas um projeto específico pelo seu ID. Na tela, exiba o Título, a Descrição, a Categoria e faça uma lista com os nomes de todos os alunos que integram a equipe deste projeto.
- **Tela de Detalhes do Aluno**: Crie uma view que, ao clicar no aluno em detalhes do projeto, apresente os detalhes do aluno selecionado. Apresente nome, matrícula e a lista de projetos do aluno.

💡 Dica do Professor: Como o atributo "equipe" é um relacionamento de muitos para muitos (ManyToMany), você precisará utilizar o sufixo `.all` dentro do laço de repetição no seu template HTML. Exemplo: `{% for aluno in projeto.equipe.all %}`.

## 5. Enviar para o GitHub

Após a conclusão do projeto, crie um repositório no github e envie os arquivos do projeto.

A atividade é individual e você deve hospedar o seu projeto em sua conta no github.

## 6. Checklist de Entrega e Avaliação

Ao finalizar a atividade, chame o professor para apresentar os seguintes itens na sua máquina:

- [ ] Código do arquivo `models.py` contendo os relacionamentos 1:1, 1:N e N:M.
- [ ] Painel Django Admin acessível e contendo os dados cadastrados.
- [ ] Acesso à URL da tela de listagem renderizando os títulos dos projetos.
- [ ] Acesso à URL da tela de detalhes renderizando corretamente os membros da equipe.

