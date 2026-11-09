"""Gera o .docx da Aula 1 (mesmo conteúdo do .tex). Uso: python docx_aula1.py <saida.docx>"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_base import Entrega  # noqa: E402

e = Entrega()
e.cabecalho("Aula 1 · 26/10 · Entender o problema e definir o escopo")

e.secao("1. O problema")
e.par("A coordenação da faculdade recebia pedidos de laboratório por e-mail e dois professores chegavam para o "
      "mesmo horário. A faculdade tem quatro laboratórios: o Lab 202 tem 30 lugares e os demais (Lab 101, Lab 102 "
      "e Lab 201) têm 40. A faculdade abre de segunda a sexta das 07:00 às 22:00 e aos sábados até 12:00. O sistema "
      "deve mostrar a agenda dos laboratórios, permitir reservar e impedir choques de horário.")
e.par("A equipe usou a versão 1.0 do sistema, no Laboratório de Sistemas, por 20 minutos como se fosse o cliente, "
      "e separou os requisitos que o sistema já atende dos que ainda faltam.")

e.secao("2. Requisitos funcionais")
e.rico([("A coluna ", False), ("Regras", False, True),
        (" indica as regras de negócio da tela do sistema (RN01 a RN18) ligadas a cada requisito. Os requisitos "
         "RF06 a RF10 não existem na versão 1.0 e, por isso, ainda não têm regras na tela.", False)])
parcial = lambda n: [(f"Atende parcialmente{n}", True)]  # noqa: E731
falta = [("Falta", True)]
e.tabela(["Código", "Requisito", "Regras", "Versão 1.0"], [
    ["RF01", "Cadastrar uma reserva com professor, disciplina, laboratório, data, horário de início, duração e "
             "número de alunos.", "RN01 a RN06, RN09 a RN13", "Atende"],
    ["RF02", "Impedir reservas com horários sobrepostos no mesmo laboratório.", "RN07", parcial("¹")],
    ["RF03", "Cancelar ou excluir uma reserva, liberando o horário para outros professores.", "RN08, RN18", parcial("²")],
    ["RF04", "Listar as reservas por data e horário e buscar pelo nome do professor ou pela disciplina.",
     "RN14, RN15, RN17", parcial("³")],
    ["RF05", "Mostrar a ocupação de cada laboratório no dia seguinte.", "RN16", parcial("⁴")],
    ["RF06", "Exibir a agenda de cada laboratório em grade (dia × horário), destacando os horários livres.", "–", falta],
    ["RF07", "Consultar a disponibilidade de um laboratório antes de preencher a reserva.", "–", falta],
    ["RF08", "Editar uma reserva já feita (data, horário ou laboratório).", "–", falta],
    ["RF09", "Identificar o usuário por login, separando o perfil de professor do perfil da coordenação.", "–", falta],
    ["RF10", "Notificar o professor por e-mail quando a reserva for confirmada ou cancelada.", "–", falta],
], [1.6, 7.6, 2.9, 2.9], centro=(0, 2, 3))
for nota in [
    "¹ RF02 (RN07): bloqueia apenas reservas com o mesmo horário de início. Reservas cujos horários se cruzam "
    "são aceitas (exemplo: Lab 101, 06/11/2026, das 19:00 às 22:00 e das 20:00 às 21:00).",
    "² RF03 (RN08): a reserva é cancelada, mas o horário não é liberado. Uma nova reserva no mesmo laboratório, "
    "data e horário é recusada com a mensagem “já está reservado nesse horário”.",
    "³ RF04 (RN15): a busca encontra pelo nome do professor, mas não pela disciplina.",
    "⁴ RF05 (RN16): o painel Ocupação de amanhã soma também as horas das reservas canceladas.",
]:
    e.par(nota, size=10, after=3)

e.secao("3. Requisitos não funcionais (qualidades)")
e.tabela(["Código", "Qualidade", "Descrição"], [
    ["RNF01", "Usabilidade", "Ser fácil de usar no celular: um professor faz uma reserva em menos de 2 minutos, sem treinamento."],
    ["RNF02", "Desempenho", "Mostrar a agenda e o resultado da busca em até 2 segundos."],
    ["RNF03", "Segurança", "Permitir que apenas a coordenação exclua ou altere reservas de outros professores."],
], [1.8, 2.8, 10.4], centro=(0,))

e.secao("4. O que fica fora do sistema")
e.lista(["Controle de presença dos alunos nas aulas.",
         "Manutenção e inventário dos computadores dos laboratórios.",
         "Reserva de outros espaços da faculdade, como auditório e salas comuns.",
         "Integração com o sistema acadêmico da faculdade (matrículas e notas).",
         "Acesso de alunos ao sistema (consulta ou reserva de laboratórios)."])

e.secao("5. Histórias de usuário")
e.par("Cada história foi escrita a partir de um dos requisitos da Seção 2.")
hist = lambda quem, resto: [("Como ", False), (quem, True), (resto, False)]  # noqa: E731
e.tabela(["Nº", "História", "Requisito"], [
    ["H01", hist("professor", ", quero ver a agenda de um laboratório, para escolher um horário livre sem tentar várias vezes."), "RF06"],
    ["H02", hist("professor", ", quero reservar um laboratório pelo celular, para não precisar mandar e-mail para a coordenação."), "RF01"],
    ["H03", hist("professor", ", quero cancelar minha reserva, para liberar o laboratório para outro colega."), "RF03"],
    ["H04", hist("professor", ", quero alterar a data ou o horário da reserva, para não precisar cancelar e criar outra."), "RF08"],
    ["H05", hist("coordenação", ", quero buscar as reservas de um professor ou disciplina, para resolver dúvidas rapidamente."), "RF04"],
    ["H06", hist("professor", ", quero receber um aviso quando a reserva for confirmada, para ter certeza de que o laboratório está garantido."), "RF10"],
], [1.5, 11.3, 2.2], centro=(0, 2))

e.salvar(sys.argv[1])
