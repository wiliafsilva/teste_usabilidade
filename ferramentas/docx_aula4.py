"""Gera o .docx da Aula 4 (mesmo conteúdo do .tex). Uso: python docx_aula4.py <saida.docx> <pasta figuras>"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_base import REFS, Entrega  # noqa: E402

saida, fig = sys.argv[1], sys.argv[2]
e = Entrega()
e.cabecalho("Aula 4 · 23/11 · Escolher a solução e organizar os dados")

# 1. Comparação
e.secao("1. Comparação de duas formas de construir o sistema")
e.rico([("Foram comparadas duas opções para a versão 2.0: um ", False), ("aplicativo instalado", False, True),
        (" no celular (Android e iPhone) e um ", False), ("site que abre no celular", False, True),
        (", isto é, um site responsivo que se adapta à tela do celular e do computador.", False)])
e.tabela(["Critério", "Aplicativo instalado", "Site que abre no celular"], [
    ["Custo",
     "Mais alto: é preciso fazer e manter versões para Android e iPhone e pagar as contas das lojas (Google Play: "
     "taxa única de US$ 25; Apple: US$ 99 por ano).",
     "Mais baixo: um único código serve para celular e computador; o custo principal é a hospedagem."],
    ["Facilidade para o usuário",
     "O professor precisa encontrar, baixar e instalar o aplicativo antes da primeira reserva; ocupa espaço para um "
     "uso de poucas vezes por semana.",
     "Abre por um link, sem instalar nada. Funciona no celular e no computador da sala de aula."],
    ["Manutenção",
     "Cada correção passa pela revisão das lojas e só chega a quem atualizar o aplicativo; podem existir várias "
     "versões em uso ao mesmo tempo.",
     "A correção é feita no servidor e vale na hora para todos os usuários; existe uma só versão em uso."],
    ["Uso pela coordenação",
     "A coordenação trabalha no computador; seria preciso fazer também uma versão para computador.",
     "O mesmo site atende professores no celular e a coordenação no computador."],
    ["Avisos ao professor", "Pode enviar notificações no próprio celular.",
     "Envia os avisos por e-mail (RF10), o que já atende ao caso."],
], [3.2, 5.9, 5.9])

# 2. Escolha
e.secao("2. Solução escolhida e justificativa")
e.rico([("A solução escolhida é o ", False), ("site que abre no celular", True), (".", False)])
e.rico([("O problema do caso é que a coordenação recebia os pedidos de laboratório por e-mail e dois professores "
         "chegavam para o mesmo horário. Para resolver isso, todos precisam consultar e alterar ", False),
        ("a mesma agenda, ao mesmo tempo", False, True),
        (": quando um professor reserva o Lab 101, o horário deve aparecer ocupado na hora para todos os outros. Um "
         "site ligado a um único servidor garante isso de forma simples, para quem está no celular e para quem está "
         "no computador.", False)])
e.par("Além disso, o professor reserva laboratório poucas vezes por semana. Exigir que ele instale um aplicativo "
      "cria uma barreira que pode fazê-lo voltar a pedir por e-mail, que é exatamente o risco R04 da Aula 2 e o "
      "contrário do RNF01 (fazer uma reserva em menos de 2 minutos, sem treinamento). O site também tem menor custo "
      "e manutenção mais simples, e a versão 1.0 já funciona no navegador, o que facilita a migração dos dados "
      "(risco R01). A única vantagem clara do aplicativo, as notificações no celular, é coberta pelos avisos por "
      "e-mail previstos no RF10.")

# 3. Dados
e.secao("3. Informações que o sistema guarda")
e.rico([("As informações foram levantadas a partir dos campos do formulário ", False), ("Nova reserva", False, True),
        (" e das colunas da tabela ", False), ("Registros", False, True),
        (" da versão 1.0, e agrupadas por assunto. A Figura 1 mostra os grupos ligados por setas; o sinal ", False),
        ("+", True), (" marca o que precisa ser acrescentado na versão 2.0.", False)])
e.imagens([f"{fig}/dados.png"], 15)
e.legenda("Figura 1. Informações que o sistema guarda, agrupadas por assunto.")
acr = lambda t: [("Acrescentar", True), (t, False)]  # noqa: E731
e.tabela(["Grupo", "Informação", "Onde aparece na versão 1.0", "Versão 2.0"], [
    ["Reserva", "Professor", "Campo do formulário e coluna Professor", "Passa a vir do usuário que fez login (RF09)."],
    ["Reserva", "Disciplina", "Campo do formulário e coluna Disciplina", "Mantém."],
    ["Reserva", "Laboratório", "Campo (lista) e coluna Laboratório", "Mantém, ligado ao grupo Laboratório."],
    ["Reserva", "Data", "Campo do formulário e coluna Data", "Mantém."],
    ["Reserva", "Início", "Campo (lista) e coluna Horário", "Mantém."],
    ["Reserva", "Duração em horas", "Campo do formulário", "Mantém."],
    ["Reserva", "Término", "Calculado (início + duração) e mostrado na coluna Horário", "Mantém, calculado."],
    ["Reserva", "Número de alunos", "Campo do formulário e coluna Alunos", "Mantém."],
    ["Reserva", "Situação", "Coluna Situação (Reservado ou Cancelada)", "Mantém."],
    ["Reserva", "Data de criação", "Guardada pelo sistema, sem aparecer na tela", "Mantém."],
    ["Reserva", "Datas de alteração e de cancelamento", "Não existem", acr(" (RF08 e RF03).")],
    ["Laboratório", "Nome e capacidade", "Fixos no sistema: Lab 202 com 30 lugares e os demais com 40",
     acr(" um cadastro próprio, para mudar a capacidade sem alterar o código.")],
    ["Usuário", "Nome, e-mail, senha e perfil", "Não existem", acr(" (RF09 e RNF03).")],
    ["Aviso", "Reserva, e-mail, tipo e data de envio", "Não existem", acr(" (RF10).")],
], [2.4, 3.4, 4.6, 4.6])

# 4. Fundamentação
e.secao("4. Artigo: fundamentação teórica")
e.par("Tema 6 · Teste de usabilidade em aplicativos", bold=True)
blocos = [
    ("Usabilidade", [
        [("Barbosa e Silva (2010) apresentam a usabilidade como um dos principais critérios de qualidade de uso de um "
          "sistema interativo. Com base na norma ISO 9241-11, os autores a descrevem como o grau em que um produto pode "
          "ser usado por usuários específicos para alcançar objetivos específicos com eficácia, eficiência e "
          "satisfação, em um contexto de uso determinado. A eficácia indica se o usuário consegue concluir a tarefa; a "
          "eficiência, quanto tempo e esforço ele gasta para isso; e a satisfação, como ele se sente ao usar o "
          "sistema.", False)],
        [("Essas três dimensões mostram que um sistema não é fácil de usar apenas por funcionar: ele precisa ser "
          "compreendido logo no "
          "primeiro uso, evitar que o usuário cometa erros e permitir que ele se recupere quando os erros acontecem. No "
          "sistema de reserva de laboratórios, por exemplo, uma regra correta, como o limite de 1 a 4 horas por "
          "reserva, pode gerar frustração se o professor só descobrir esse limite depois de preencher todo o "
          "formulário.", False)],
    ]),
    ("Teste de usabilidade com usuários", [
        [("Barbosa e Silva (2010) distinguem os métodos de avaliação feitos por especialistas, que inspecionam a "
          "interface, dos métodos de observação, em que pessoas representativas do público-alvo usam o sistema. No "
          "teste de usabilidade, o avaliador prepara tarefas realistas, observa os participantes enquanto eles as "
          "executam e registra dados como o sucesso na tarefa, o tempo gasto e os erros cometidos. É comum pedir que o "
          "participante pense em voz alta, explicando o que está tentando fazer, o que ajuda a entender a causa das "
          "dificuldades, e não apenas o seu efeito.", False)],
        [("A quantidade de participantes é uma dúvida frequente. Nielsen e Landauer (1993) propuseram um modelo "
          "matemático em que a proporção de problemas encontrados depois de i participantes é 1 − (1 − λ)", False),
         ("i", False, True),
         (", sendo λ a probabilidade de um único participante revelar um problema qualquer. Nos projetos analisados "
          "pelos autores, λ ficou, em média, em torno de 31%. Com esse valor, cinco participantes revelam cerca de 85% "
          "dos problemas, e cada participante a mais traz cada vez menos descobertas novas. Os autores também mostram, "
          "numa análise de custo e benefício, que o melhor retorno está em testes com poucos participantes, repetidos "
          "depois de cada rodada de correções. O resultado, porém, depende de λ, que muda de um sistema para outro; os "
          "cinco participantes são uma referência prática, e não uma garantia.", False)],
    ]),
    ("Questionário SUS", [
        [("A ", False), ("System Usability Scale", False, True),
         (" (SUS) foi proposta por Brooke (1996) como uma forma rápida e barata de medir a percepção de usabilidade de "
          "um sistema. O questionário tem dez afirmações, respondidas numa escala de 1 (discordo totalmente) a 5 "
          "(concordo totalmente), alternando afirmações positivas (itens ímpares) e negativas (itens pares). Para "
          "calcular a nota, subtrai-se 1 da resposta de cada item ímpar e subtrai-se de 5 a resposta de cada item par; "
          "a soma desses valores é multiplicada por 2,5, o que gera uma nota de 0 a 100 (BROOKE, 1996). Essa nota não "
          "é uma porcentagem: ela só tem sentido quando comparada a uma referência.", False)],
        [("Essa referência foi construída por Bangor, Kortum e Miller (2008), que analisaram mais de dois mil "
          "questionários SUS aplicados em cerca de duzentos testes de usabilidade, ao longo de dez anos. Os autores "
          "confirmaram a alta confiabilidade do questionário e encontraram uma nota média próxima de 70. Com base "
          "nisso, propuseram faixas de aceitabilidade: notas abaixo de 50 indicam usabilidade inaceitável; entre 50 e "
          "70, marginal; e acima de 70, aceitável (BANGOR; KORTUM; MILLER, 2008). Neste estudo, essas faixas são "
          "usadas para interpretar a nota obtida pelo sistema.", False)],
    ]),
    ("Heurísticas de usabilidade", [
        [("Nielsen e Molich (1990) propuseram a avaliação heurística, em que avaliadores examinam a interface com base "
          "em um pequeno conjunto de princípios gerais, chamados heurísticas. As nove heurísticas originais são: "
          "diálogo simples e natural; falar a língua do usuário; minimizar a carga de memória do usuário; ser "
          "consistente; fornecer ", False), ("feedback", False, True),
         ("; oferecer saídas claramente marcadas; oferecer atalhos; fornecer boas mensagens de erro; e prevenir erros. "
          "Os autores observaram que cada avaliador, sozinho, encontrou apenas de 20% a 51% dos problemas, e que juntar "
          "os resultados de vários avaliadores aumenta bastante a quantidade de problemas encontrados (NIELSEN; "
          "MOLICH, 1990).", False)],
        [("Neste trabalho, as heurísticas não são usadas como um método de avaliação separado, mas como vocabulário "
          "para classificar os problemas observados no teste com usuários. Cada problema também é classificado pelo "
          "impacto que teve na tarefa observada: ", False), ("alto", False, True),
         (", quando impediu o participante de concluí-la; ", False), ("médio", False, True),
         (", quando a atrasou ou exigiu uma nova tentativa; e ", False), ("baixo", False, True),
         (", quando causou apenas dúvida ou incômodo. Essa classificação ajuda a decidir quais correções devem entrar "
          "primeiro na versão 2.0.", False)],
    ]),
    ("Síntese", [
        [("Combinadas, essas referências orientam o método deste estudo: as tarefas observadas medem a eficácia (taxa "
          "de sucesso) e a eficiência (tempo) do uso; o questionário SUS mede a satisfação; e as heurísticas, com a "
          "classificação por impacto, organizam os problemas encontrados numa lista de melhorias para a versão 2.0.",
          False)],
    ]),
]
for titulo, paragrafos in blocos:
    e.par(titulo, bold=True)
    for partes in paragrafos:
        e.rico(partes, just=True)

e.secao("Referências citadas na fundamentação", size=12)
for k in ["F4", "F5", "F3", "F1", "F2"]:
    e.rico(REFS[k], size=10)

e.salvar(saida)
