"""Gera o .docx do kit do teste de usabilidade (mesmo conteúdo do .tex). Uso: python docx_kit.py <saida.docx>"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.shared import Cm, Pt  # noqa: E402
from docx_base import Entrega  # noqa: E402

CX = "☐"
e = Entrega()
for s in e.doc.sections:
    s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(2.5)
quebra = e.doc.add_page_break


def numerada(itens):
    for partes in itens:
        e.rico(partes if isinstance(partes, list) else [(partes, False)], style="List Number")


# ---------------- capa ----------------
e.par("ARTIGO · TEMA 6 · TESTE DE USABILIDADE EM APLICATIVOS", bold=True, size=10, center=True, after=2)
e.par("Kit do teste de usabilidade", bold=True, size=18, center=True, after=4)
e.par("Sistema de reserva de laboratórios (Caso 15, versão 1.0) · no celular", size=13, center=True, after=2)
e.par("Responsável: Wilia Francisco da Silva", center=True, after=12)

e.secao("O que imprimir", size=14)
e.tabela(["Parte", "Para quem", "Cópias"], [
    ["1. Roteiro do condutor (com gabarito)", "Você", "1"],
    ["2. Termo de consentimento", "Cada participante assina antes de começar", "5"],
    ["3. Cartões das tarefas", "O participante lê um cartão por vez", "1 jogo"],
    ["4. Ficha de observação", "Você preenche durante o teste", "5"],
    ["5. Questionário SUS", "O participante responde no final", "5"],
], [6, 7.5, 2.5], centro=(2,))
e.rico([("Depois do teste, as respostas vão para a ", False), ("Planilha do teste de usabilidade.xlsx", True),
        (", que calcula a nota SUS, a taxa de sucesso e o tempo médio.", False)])

e.secao("Preparação (antes do primeiro participante)", size=14)
numerada([
    [("Envie o arquivo laboratorio-de-sistemas.html para o celular que será usado (por WhatsApp, e-mail ou cabo) e "
      "abra no navegador. Ele funciona sem internet depois de aberto.", False)],
    [("Na página inicial, toque no ", False), ("caso 15", True),
     (" e confira que a tela Reserva de laboratórios abre.", False)],
    [("Tenha um ", False), ("cronômetro", True), (" (o do próprio celular de quem conduz), caneta e as cópias impressas.", False)],
    [("Escolha um lugar calmo. Cada sessão leva cerca de ", False), ("20 minutos", True), (".", False)],
    [("Antes de cada participante", True), (", toque em ", False), ("Restaurar dados de exemplo", False, True),
     (", no fim da tela, para que todos comecem com os mesmos dados.", False)],
])
e.secao("Participantes", size=14)
e.rico([("Cinco colegas de curso, que farão o papel de ", False), ("professor", True),
        (" que precisa reservar laboratório. Eles devem ser identificados apenas como ", False), ("P1 a P5", True),
        (" em todos os papéis e na planilha.", False)])

# ---------------- 1. roteiro ----------------
quebra()
e.secao("1. Roteiro do condutor", size=14)
e.par("Antes de começar (cerca de 3 minutos)", bold=True)
e.par("Leia em voz alta, com suas palavras:")
p = e.rico([("“Obrigado por participar. Estou testando um sistema de reserva de laboratórios da faculdade, para um "
             "artigo da disciplina. ", False), ("Quem está sendo avaliado é o sistema, não você", True),
            (": se algo der errado, é um problema do sistema, e isso me ajuda muito. Vou te entregar algumas tarefas, "
             "uma de cada vez. Imagine que você é um professor da faculdade. Enquanto usa o sistema, ", False),
            ("pense em voz alta", True),
            (": diga o que está procurando, o que espera que aconteça e o que achou estranho. Eu não posso te ajudar "
             "durante as tarefas, mas você pode desistir de qualquer uma quando quiser. Quando terminar uma tarefa, me "
             "avise dizendo ‘terminei’.”", False)])
p.paragraph_format.left_indent = p.paragraph_format.right_indent = Cm(1)
numerada([
    [("Peça para o participante ler e assinar o ", False), ("termo de consentimento", True), (".", False)],
    "Anote na ficha o número do participante (P1 a P5) e o modelo do celular.",
    "Confirme que os dados de exemplo foram restaurados e entregue o celular já na tela do caso 15.",
])
e.par("Durante as tarefas (cerca de 12 minutos)", bold=True)
numerada([
    [("Entregue o cartão da tarefa, deixe o participante ler e ", False), ("comece o cronômetro", True),
     (" quando ele tocar na tela.", False)],
    [("Não ajude e não aponte para a tela.", True),
     (" Se ele ficar em silêncio, pergunte só: “O que você está pensando agora?”. Se ele perguntar algo, devolva: "
      "“O que você acha?”.", False)],
    [("Pare o cronômetro", True), (" quando ele disser “terminei” ou desistir, ou quando chegar a ", False),
     ("5 minutos", True), (" (nesse caso, a tarefa conta como falha).", False)],
    [("Anote na ficha: o tempo, o resultado, os erros e as falas importantes. Um ", False), ("erro", False, True),
     (" é qualquer ação que o afasta do objetivo: tocar no botão errado, preencher um campo errado, receber uma "
      "mensagem de erro.", False)],
    [("Se for preciso ajudar para ele conseguir seguir para a próxima tarefa, marque ", False),
     ("Sucesso com ajuda", False, True), (".", False)],
])
e.par("Depois das tarefas (cerca de 5 minutos)", bold=True)
numerada([
    [("Entregue o ", False), ("questionário SUS", True),
     (" e peça que responda pensando no sistema que acabou de usar, sem pensar muito em cada item.", False)],
    "Faça as duas perguntas finais e anote na ficha: “O que você achou mais fácil?” e “O que mais te atrapalhou?”.",
    [("Agradeça. Antes do próximo participante, toque em ", False), ("Restaurar dados de exemplo", False, True), (".", False)],
])
e.par("Gabarito das tarefas (só para o condutor)", bold=True)
e.tabela(["Tarefa", "Conta como sucesso quando", "O que observar"], [
    ["1", [("Aparece na lista uma reserva do ", False), ("Lab 201", True), (", na ", False),
           ("próxima quinta-feira", True), (", ", False), ("10:00 às 12:00", True),
           (", Estrutura de Dados, 30 alunos, em nome da Profa. Ana Souza.", False)],
     "Se entende o campo Duração em horas (precisa digitar 2); se as mensagens de erro ajudam a corrigir."],
    ["2", [("O participante informa a primeira reserva do Lab 101: ", False), ("Prof. Danilo Rezende", True),
           (", Algoritmos, no próximo dia útil, ", False), ("08:00 às 12:00", True), (".", False)],
     "Como procura (rola a lista, usa a busca?); quanto tempo leva para achar."],
    ["3", [("O participante faz uma reserva que ", False), ("respeita as regras da tela", True),
           (" (no sábado, a reserva termina até 12:00; 35 alunos não cabem no Lab 202) ", False), ("ou", True),
           (" explica por que o pedido, como está, não pode ser feito e propõe uma alternativa.", False)],
     "Se lê as regras de negócio; se percebe o limite de sábado; o que o sistema faz quando a regra é desrespeitada."],
    ["4", [("A reserva da tarefa 1 aparece com a situação ", False), ("Cancelada", True), (".", False)],
     "Se confunde Cancelar com Excluir; se sente falta de confirmação."],
    ["5", [("O participante informa ", False), ("Lab 101", True), (", a data e ", False), ("19:00 às 22:00", True), (".", False)],
     "Que palavra digita na busca (professor ou disciplina) e o que faz se a busca não encontrar nada."],
], [1.6, 7.7, 6.7], centro=(0,))

# ---------------- 2. termo ----------------
quebra()
e.secao("2. Termo de consentimento livre e esclarecido", size=14)
for rot, txt in [
    ("Pesquisa: ", "Teste de usabilidade de um sistema de reserva de laboratórios (artigo da disciplina Laboratório "
                   "de Engenharia de Software, Universidade Tiradentes)."),
    ("Responsável: ", "Wilia Francisco da Silva (wilia.francisco@souunit.com.br)."),
    ("Objetivo: ", "avaliar se o sistema é fácil de usar. Quem está sendo avaliado é o sistema, e não o participante."),
    ("Como funciona: ", "você vai usar o sistema num celular para realizar 5 tarefas curtas, pensando em voz alta, e "
                       "depois responder a um questionário de 10 perguntas. A sessão leva cerca de 20 minutos. O "
                       "responsável vai anotar o tempo, os erros e os comentários."),
]:
    e.rico([(rot, True), (txt, False)])
e.par("Seus direitos:", bold=True)
e.lista(["A participação é voluntária e não tem custo nem pagamento.",
         "Você pode desistir a qualquer momento, sem precisar explicar o motivo.",
         "Seu nome não aparecerá no artigo. Você será identificado apenas por um código (P1 a P5).",
         "Os dados serão usados somente neste trabalho acadêmico.",
         "Não haverá gravação de áudio, vídeo ou imagem do seu rosto."])
e.par("Declaro que li as informações acima, que minhas dúvidas foram esclarecidas e que concordo em participar.")
e.par("")
e.par("Código do participante: ________        Data: ____/____/2026")
e.par("")
e.par("")
e.par("______________________________________\nAssinatura do participante")
e.par("")
e.par("______________________________________\nWilia Francisco da Silva (responsável)")

# ---------------- 3. cartões ----------------
quebra()
e.secao("3. Cartões das tarefas", size=14)
e.par("Recorte nas linhas e entregue um cartão por vez, na ordem.", size=10)
cartoes = [
    [("Você é a ", False), ("Profa. Ana Souza", True), (". Na ", False), ("próxima quinta-feira", True), (", das ", False),
     ("10h às 12h", True), (", você vai dar aula de ", False), ("Estrutura de Dados", True), (" para ", False),
     ("30 alunos", True), (" no ", False), ("Lab 201", True), (". Faça essa reserva.", False)],
    [("Você vai usar o ", False), ("Lab 101", True), (" e quer saber se ele já está ocupado. Descubra qual é a ", False),
     ("primeira reserva", True), (" do Lab 101 que existe no sistema: em que dia, de que horas a que horas e de qual "
                                  "professor.", False)],
    [("Você precisa de um laboratório para a disciplina de ", False), ("Banco de Dados II", True), (", com ", False),
     ("35 alunos", True), (", no ", False), ("próximo sábado", True), (", das ", False), ("10h às 13h", True),
     (". Faça a reserva.", False)],
    [("A aula de Estrutura de Dados da Profa. Ana Souza (tarefa 1) foi suspensa. ", False),
     ("Cancele essa reserva", True), (".", False)],
    [("A coordenação quer saber em que laboratório e em que horário será a aula de ", False), ("Banco de Dados", True),
     (" do ", False), ("Prof. Sérgio Santana", True), (". Encontre essa reserva ", False), ("usando a busca", True),
     (".", False)],
]
for k, partes in enumerate(cartoes, 1):
    t = e.doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    c = t.rows[0].cells[0]
    r = c.paragraphs[0].add_run(f"Tarefa {k}")
    r.bold = True
    r.font.size = Pt(14)
    p = c.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    for parte in partes:
        r = p.add_run(parte[0])
        r.bold = parte[1]
        r.font.size = Pt(14)
    e.doc.add_paragraph()

# ---------------- 4. ficha ----------------
quebra()
e.secao("4. Ficha de observação", size=14)
e.par("Participante: P____        Data: ____/____/2026")
e.par("Celular (modelo): ______________________________")
e.par(f"Já reservou laboratório ou sala por algum sistema?   {CX} Sim   {CX} Não")
res = f"{CX} Sucesso\n{CX} Sucesso com ajuda\n{CX} Falha"
e.tabela(["Tarefa", "Tempo", "Resultado", "Erros", "Observações e falas"],
         [[str(k), "___:___", res, "", ""] for k in range(1, 6)], [1.5, 2, 4.3, 1.5, 6.7], centro=(0, 1))
e.par("Tempo em minutos:segundos. Limite de 5 minutos por tarefa (passou disso, marque Falha).", size=10)
e.par("Problemas observados (o que atrapalhou o participante)", bold=True)
imp = f"{CX} Alto {CX} Médio {CX} Baixo"
e.tabela(["Tarefa", "O que aconteceu", "Impacto"], [["", "", imp]] * 3, [1.5, 10, 4.5])
e.rico([("Impacto: ", False), ("alto", True), (" = impediu de concluir; ", False), ("médio", True),
        (" = atrasou ou exigiu nova tentativa; ", False), ("baixo", True), (" = só causou dúvida ou incômodo.", False)],
       size=10)
e.par("O que achou mais fácil?", bold=True)
e.par("_" * 80)
e.par("O que mais atrapalhou?", bold=True)
e.par("_" * 80)

# ---------------- 5. SUS ----------------
quebra()
e.secao("5. Questionário SUS", size=14)
e.par("Participante: P____        Data: ____/____/2026")
e.rico([("Pensando no sistema de reserva de laboratórios que você acabou de usar, marque ", False),
        ("um número", True), (" em cada frase. Responda rápido, sem pensar muito. Se não souber responder uma frase, "
                              "marque o 3.", False)])
e.par("1 = discordo totalmente        5 = concordo totalmente", center=True)
SUS = [
    "Eu acho que gostaria de usar este sistema com frequência.",
    "Eu achei o sistema desnecessariamente complexo.",
    "Eu achei o sistema fácil de usar.",
    "Eu acho que precisaria da ajuda de uma pessoa com conhecimentos técnicos para usar este sistema.",
    "Eu achei que as várias funções deste sistema estão bem integradas.",
    "Eu achei que há muita inconsistência neste sistema.",
    "Eu imagino que a maioria das pessoas aprenderia a usar este sistema rapidamente.",
    "Eu achei o sistema muito complicado de usar.",
    "Eu me senti muito confiante usando o sistema.",
    "Eu precisei aprender muitas coisas antes de conseguir usar este sistema.",
]
e.tabela(["Nº", "Afirmação", "1", "2", "3", "4", "5"],
         [[str(k), txt, CX, CX, CX, CX, CX] for k, txt in enumerate(SUS, 1)],
         [1, 10, 1, 1, 1, 1, 1], centro=(0, 2, 3, 4, 5, 6))
p = e.par("Questionário baseado na System Usability Scale (BROOKE, 1996), em tradução livre para o português.",
          size=9, italic=True)
p.alignment = WD_ALIGN_PARAGRAPH.LEFT

e.salvar(sys.argv[1])
