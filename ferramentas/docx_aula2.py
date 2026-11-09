"""Gera o .docx da Aula 2 (mesmo conteúdo do .tex). Uso: python docx_aula2.py <saida.docx>"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_base import REFS, Entrega  # noqa: E402

e = Entrega()
e.cabecalho("Aula 2 · 09/11 · Planejar o trabalho")

e.secao("1. Tarefas da versão 2.0")
e.par("As histórias da Aula 1 foram quebradas em tarefas menores. Cada requisito que falta na versão 1.0 (RF06 a "
      "RF10) virou trabalho da versão 2.0. Os requisitos atendidos apenas parcialmente (RF02 a RF05) viraram a "
      "tarefa T14, que corrige os defeitos encontrados. O responsável por todas as tarefas é o único integrante "
      "da equipe.")
tarefas = [
    ("T01", "Criar a tela de login com usuário e senha.", "RF09", "1"),
    ("T02", "Separar os perfis de professor e de coordenação.", "RF09, RNF03", "1"),
    ("T03", "Fazer cópia de segurança das reservas atuais e migrar os dados para a versão 2.0.", "Risco R01", "1"),
    ("T04", "Desenhar a grade da agenda (dia × horário) de cada laboratório.", "H01, RF06", "2"),
    ("T05", "Destacar na grade os horários livres e os ocupados.", "H01, RF06", "2"),
    ("T06", "Mostrar a disponibilidade ao escolher laboratório e data no formulário.", "H01, RF07", "2"),
    ("T07", "Ajustar o formulário e a agenda para telas de celular.", "H02, RNF01", "2"),
    ("T08", "Criar o botão Editar na lista de reservas.", "H04, RF08", "3"),
    ("T09", "Validar as regras de negócio também ao editar (choque de horário, capacidade e horário de "
            "funcionamento).", "H04, RF08", "3"),
    ("T10", "Configurar o envio de e-mail do sistema.", "H06, RF10", "3"),
    ("T11", "Enviar aviso ao professor quando a reserva for confirmada ou cancelada.", "H06, RF10", "3"),
    ("T12", "Executar de novo os casos de teste da versão 1.0 e testar as funções novas.", "Risco R02", "4"),
    ("T13", "Validar as telas novas com a coordenação e publicar a versão 2.0.", "Risco R04", "4"),
    ("T14", "Corrigir os defeitos da versão 1.0: choque de horário, cancelamento que não libera o horário, busca "
            "por disciplina e painel de ocupação.", "RF02 a RF05", "1"),
]
e.tabela(["Nº", "Tarefa", "Origem", "Sem.", "Responsável"],
         [[n, t, o, s, "Wilia"] for n, t, o, s in tarefas],
         [1.3, 7.7, 2.6, 1.2, 2.2], centro=(0, 2, 3, 4))

e.secao("2. Quadro Kanban")
e.rico([("Situação do quadro no início do trabalho. Só o RF01, que a versão 1.0 atende por completo, fica na "
         "coluna ", False), ("Feito", False, True),
        (". Os requisitos RF02 a RF05 atendem apenas em parte e entram em ", False), ("A fazer", False, True),
        (" como a tarefa T14.", False)])
a_fazer = ["T14 Corrigir RF02 a RF05", "T02 Perfis de professor e coordenação", "T03 Cópia de segurança e migração",
           "T04 Grade da agenda", "T05 Horários livres e ocupados", "T06 Disponibilidade no formulário",
           "T07 Ajuste para celular", "T08 Botão Editar", "T09 Regras ao editar", "T10 Envio de e-mail",
           "T11 Aviso ao professor", "T12 Testes da versão 2.0", "T13 Validação e publicação"]
e.tabela(["A fazer", "Fazendo", "Feito"],
         [["\n".join(a_fazer), "T01 Tela de login", "RF01 Cadastrar reserva"]], [5, 5, 5])

e.secao("3. Cronograma de 4 semanas")
e.tabela(["Semana", "O que será feito", "Tarefas"], [
    ["1", "Login, perfis de acesso, cópia de segurança dos dados atuais e correção dos defeitos da versão 1.0.",
     "T01 a T03, T14"],
    ["2", "Agenda em grade, consulta de disponibilidade e ajuste para celular.", "T04 a T07"],
    ["3", "Edição de reservas e avisos por e-mail.", "T08 a T11"],
    ["4", "Testes, validação com a coordenação e publicação da versão 2.0.", "T12 e T13"],
], [1.8, 10.2, 3.0], centro=(0, 2))

e.secao("4. Riscos")
e.tabela(["Nº", "Risco", "O que fazer"], [
    ["R01", "Ao alterar o sistema que já está em uso, as reservas feitas na versão 1.0 serem perdidas ou corrompidas.",
     "Fazer cópia de segurança antes de qualquer mudança e testar a migração numa cópia dos dados (T03)."],
    ["R02", "As funções novas quebrarem o que já funciona, como o cadastro de reservas e as correções feitas na T14.",
     "Executar de novo todos os casos de teste da versão 1.0 antes de publicar (T12)."],
    ["R03", "O único integrante ficar doente ou sem tempo numa semana de entrega.",
     "Manter o quadro Kanban atualizado e deixar 2 dias de folga no fim de cada semana para recuperar atrasos."],
    ["R04", "Os professores não se adaptarem à agenda nova e voltarem a pedir laboratório por e-mail.",
     "Mostrar as telas à coordenação antes de publicar e manter o atendimento por e-mail durante a primeira semana."],
    ["R05", "Os avisos por e-mail não chegarem ou caírem na caixa de spam.",
     "Mostrar a confirmação também na tela do sistema e testar o envio com e-mails institucionais."],
], [1.3, 6.85, 6.85], centro=(0,))

e.secao("5. Artigo: fontes sobre o tema")
e.par("Tema 6 · Teste de usabilidade em aplicativos. Pergunta guia: como testar se um aplicativo é fácil de usar?")
e.tabela(["Nº", "Referência", "Uso no artigo"], [
    ["F1", REFS["F1"], "Artigo científico. Justifica o teste com 5 usuários."],
    ["F2", REFS["F2"], "Artigo científico. Base para classificar os problemas encontrados."],
    ["F3", REFS["F3"], "Questionário SUS aplicado após o teste."],
    ["F4", REFS["F4"], "Artigo científico. Interpretação da nota do SUS."],
    ["F5", REFS["F5"], "Livro em português. Conceito de usabilidade e métodos de avaliação."],
], [1.3, 8.2, 5.5], centro=(0,))

e.salvar(sys.argv[1])
