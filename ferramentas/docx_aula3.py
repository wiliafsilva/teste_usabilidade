"""Gera o .docx da Aula 3 (mesmo conteúdo do .tex). Uso: python docx_aula3.py <saida.docx> <pasta figuras>"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_base import REFS, Entrega  # noqa: E402

saida, fig = sys.argv[1], sys.argv[2]
e = Entrega()
e.cabecalho("Aula 3 · 16/11 · Desenhar as partes do sistema")

e.secao("1. O sistema em 3 camadas")
e.par("O sistema segue o modelo cliente e servidor e é dividido em três camadas. O professor usa o celular ou o "
      "computador (cliente); as regras são verificadas no servidor; as informações ficam guardadas no banco de "
      "dados. A Figura 1 mostra as camadas e como elas conversam.")
e.imagens([f"{fig}/camadas.png"], 14.5)
e.legenda("Figura 1. Arquitetura em 3 camadas do sistema de reserva de laboratórios.")
e.tabela(["Camada", "Onde fica", "O que fica nela"], [
    ["Apresentação", "Celular ou computador",
     "As telas: login, agenda do laboratório, nova reserva e minhas reservas. Exemplo: o formulário de nova reserva."],
    ["Regras de negócio", "Servidor",
     "As regras RN01 a RN18. Exemplo: verificar se a reserva tem de 1 a 4 horas, se cabe no laboratório e se não "
     "choca com outra; calcular o horário de término."],
    ["Dados", "Banco de dados", "Usuários, laboratórios e reservas. Exemplo: a reserva confirmada fica gravada aqui."],
], [3.3, 3.7, 8])
e.par("Exemplo do caminho de uma reserva:", bold=True)
for partes in [
    [("O professor preenche a tela ", False), ("Nova reserva", False, True), (" no celular e toca em ", False),
     ("Confirmar reserva", False, True), (".", False)],
    [("O pedido vai para o servidor, que verifica as regras: duração de 1 a 4 horas, até 40 alunos (30 no Lab 202), "
      "horário de funcionamento e choque com outras reservas.", False)],
    [("Se tudo estiver certo, o servidor grava a reserva no banco de dados e envia o aviso por e-mail.", False)],
    [("O servidor responde ao celular, que mostra ", False), ("Reserva confirmada", False, True),
     (". Se alguma regra falhar, a tela mostra o motivo do erro.", False)],
]:
    e.rico(partes, style="List Number")

e.secao("2. Esboço das 3 telas principais")
e.par("As três telas abaixo são da versão 2.0 e cobrem o que falta na versão 1.0: a agenda do laboratório, a "
      "consulta de disponibilidade antes de reservar e a edição das reservas.")
e.tabela(["Tela", "Histórias", "O que a tela resolve"], [
    ["1 · Agenda do laboratório", "H01", "Mostra os horários livres e ocupados de cada laboratório (RF06)."],
    ["2 · Nova reserva", "H02, H01",
     "Reserva pelo celular e mostra se o laboratório está livre antes de confirmar (RF07). A duração é escolhida "
     "numa lista de 1 a 4 horas, o que evita erros de digitação."],
    ["3 · Minhas reservas", "H03, H04, H06",
     "Cancela e edita reservas (RF03, RF08) e mostra o aviso de confirmação (RF10)."],
], [4.3, 2.7, 8], centro=(1,))
e.imagens([f"{fig}/tela1-agenda.png", f"{fig}/tela2-nova-reserva.png"], 6.2)
e.legenda("Figuras 2 e 3. Tela 1 · Agenda do laboratório (à esquerda) e Tela 2 · Nova reserva (à direita).")
e.imagens([f"{fig}/tela3-minhas-reservas.png"], 6.2)
e.legenda("Figura 4. Tela 3 · Minhas reservas.")

e.secao("3. Artigo: introdução")
e.par("Tema 6 · Teste de usabilidade em aplicativos", bold=True)
for partes in [
    [("Um sistema pode cumprir todas as funções previstas e, ainda assim, fracassar quando as pessoas que o usam não "
      "entendem o que fazer, cometem erros com frequência ou desistem da tarefa. Por isso, além de verificar se o "
      "software funciona, é preciso verificar se ele é fácil de usar. Segundo Barbosa e Silva (2010), a usabilidade "
      "está relacionada à facilidade de aprendizado e de uso de um sistema e à satisfação de quem o utiliza, e deve "
      "ser avaliada com métodos próprios ao longo do desenvolvimento.", False)],
    [("Esse cuidado vale também para sistemas pequenos, criados para resolver problemas do dia a dia. É o caso do "
      "sistema de reserva de laboratórios de uma faculdade: a coordenação recebia os pedidos por e-mail e era comum "
      "dois professores chegarem ao mesmo laboratório no mesmo horário. A versão 1.0 do sistema foi criada para "
      "mostrar as reservas e impedir esses choques. No entanto, se os professores tiverem dificuldade para reservar, "
      "a tendência é que voltem a usar o e-mail, e o problema original continua.", False)],
    [("Avaliar a usabilidade não exige, necessariamente, muitos participantes. O modelo proposto por Nielsen e "
      "Landauer (1993) mostra que a quantidade de problemas encontrados cresce rapidamente com os primeiros usuários "
      "testados e que um grupo pequeno, por volta de cinco pessoas, já revela a maior parte deles. A observação dos "
      "participantes pode ser combinada com um questionário de satisfação, como a escala SUS (BROOKE, 1996), e com a "
      "classificação dos problemas pelas heurísticas de usabilidade (NIELSEN; MOLICH, 1990).", False)],
    [("Diante disso, este artigo busca responder à pergunta: ", False),
     ("como testar se um aplicativo é fácil de usar?", False, True),
     (" Para isso, apresenta um estudo de caso em que a versão 1.0 do sistema de reserva de laboratórios foi testada "
      "por cinco colegas de curso. Os objetivos específicos são: (i) planejar tarefas que representem o uso real do "
      "sistema; (ii) medir a taxa de sucesso e o tempo de cada tarefa; (iii) aplicar o questionário SUS; e (iv) "
      "classificar os problemas encontrados e propor melhorias para a versão 2.0.", False)],
    [("O restante do texto está organizado da seguinte forma: a Seção 2 apresenta a fundamentação teórica sobre "
      "usabilidade e testes com usuários; a Seção 3 descreve o desenvolvimento do estudo e analisa os resultados; e "
      "a Seção 4 traz as considerações finais.", False)],
]:
    e.rico(partes, just=True)

e.secao("Referências citadas na introdução", size=12)
for k in ["F5", "F3", "F1", "F2"]:
    e.rico(REFS[k], size=10)

e.salvar(saida)
