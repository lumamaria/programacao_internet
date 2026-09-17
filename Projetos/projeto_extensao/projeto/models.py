from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Categoria")

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome Completo")
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula")

    def __str__(self):
        return f"{self.nome} - {self.matricula}"

class PerfilAcademico(models.Model):
    # Relacionamento 1:1
    aluno = models.OneToOneField(
        Aluno, 
        on_delete=models.CASCADE, 
        related_name="perfil",
        verbose_name="Aluno"
    )
    link_lattes = models.URLField(max_length=200, blank=True, null=True, verbose_name="Link do Lattes")
    biografia = models.TextField(blank=True, null=True, verbose_name="Biografia")

    def __str__(self):
        return f"Perfil Acadêmico: {self.aluno.nome}"

class Projeto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título do Projeto")
    descricao = models.TextField(verbose_name="Descrição")
    data_inicio = models.DateField(verbose_name="Data de Início")
    
    # Relacionamento 1:N
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.PROTECT, # Protege a exclusão de uma categoria se houver projetos vinculados
        related_name="projetos",
        verbose_name="Categoria"
    )
    
    # Relacionamento N:M
    equipe = models.ManyToManyField(
        Aluno, 
        related_name="projetos",
        verbose_name="Equipe do Projeto"
    )

    def __str__(self):
        return self.titulo