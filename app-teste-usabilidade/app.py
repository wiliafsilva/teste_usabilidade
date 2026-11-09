"""Teste de usabilidade remoto · Sistema de reserva de laboratórios (Caso 15, versão 1.0).

O participante abre o link, aceita o termo, faz 5 tarefas no sistema (embutido
na página), comenta cada uma e responde ao questionário SUS. As respostas vão
para uma planilha do Google (aba "Sessoes").

Resultados (só para a responsável): abrir o link com  ?admin=1  no final.
"""
import io
import json
import re
import time
import unicodedata
import uuid
from datetime import date, datetime, timedelta
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

AQUI = Path(__file__).parent
sistema = components.declare_component("sistema_reservas", path=str(AQUI / "componente_sistema"))

LIMITE_S = 300  # 5 minutos por tarefa
TAREFAS = [
    {"titulo": "Reservar um laboratório",
     "texto": "Você é a **Profa. Ana Souza**. Na **próxima quinta-feira**, das **10h às 12h**, você vai dar aula de "
              "**Estrutura de Dados** para **30 alunos** no **Lab 201**. Faça essa reserva.",
     "pergunta": None},
    {"titulo": "Descobrir se um laboratório está ocupado",
     "texto": "Você vai usar o **Lab 101** e quer saber se ele já está ocupado. Descubra qual é a **primeira reserva** "
              "do Lab 101 que existe no sistema: em que dia, de que horas a que horas e de qual professor.",
     "pergunta": "Qual é a primeira reserva do Lab 101? (dia, horário e professor)", "na_tarefa": True},
    {"titulo": "Reservar para uma turma grande no sábado",
     "texto": "Você precisa de um laboratório para a disciplina de **Banco de Dados II**, com **35 alunos**, no "
              "**próximo sábado**, das **10h às 13h**. Faça a reserva.",
     "pergunta": "Conseguiu reservar como foi pedido? Se precisou mudar alguma coisa, conte o quê e por quê."},
    {"titulo": "Cancelar uma reserva",
     "texto": "A aula de Estrutura de Dados da Profa. Ana Souza (tarefa 1) foi suspensa. **Cancele essa reserva**.",
     "pergunta": None},
    {"titulo": "Encontrar uma aula pela busca",
     "texto": "A coordenação quer saber em que laboratório e em que horário será a aula de **Banco de Dados** do "
              "**Prof. Sérgio Santana**. Encontre essa reserva **usando a busca**.",
     "pergunta": "Em que laboratório e em que horário será a aula?", "na_tarefa": True},
]
# Respostas prontas da tela de opinião (o participante marca quantas quiser).
DIFICULDADES = [
    "Não tive dificuldade",
    "Não sabia por onde começar",
    "Não entendi o que algum campo pedia",
    "A mensagem de erro não me ajudou a corrigir",
    "Não encontrei a informação que eu procurava",
    "A busca não encontrou o que eu digitei",
    "Tive que arrastar a tabela para o lado para ver tudo",
    "Fiquei em dúvida se a minha ação tinha funcionado",
    "Tive medo de tocar no botão errado",
    "O sistema aceitou algo que eu achava que não devia",
    "Achei a tela confusa ou com informação demais",
]
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
CABECALHO = (["data_hora", "nome", "aparelho", "ja_reservou", "sessao"]
             + [f"t{n}_{c}" for n in range(1, 6)
                for c in ("resultado", "tempo_s", "erros", "resposta", "dificuldades", "comentario")]
             + [f"sus_q{q}" for q in range(1, 11)]
             + ["sus_nota", "mais_facil", "mais_atrapalhou", "reservas_final"])

st.set_page_config(page_title="Teste de usabilidade · Reserva de laboratórios", page_icon="🧪", layout="centered")
# Cartão da tarefa preso no topo enquanto o participante rola o sistema embutido.
st.markdown("""<style>
  .st-key-cartao { position: sticky; top: 3.75rem; z-index: 999; background: #ffffff;
                   padding: .4rem 0 .5rem; border-bottom: 2px solid #d0d7de; }
  .st-key-cartao .stAlert p { font-size: .92rem; margin: 0; }
</style>""", unsafe_allow_html=True)


# ---------------------------------------------------------------- planilha do Google
@st.cache_resource
def aba_sessoes():
    import gspread
    gc = gspread.service_account_from_dict(dict(st.secrets["gcp_service_account"]))
    sh = gc.open_by_url(st.secrets["planilha_url"])
    try:
        ws = sh.worksheet("Sessoes")
    except gspread.WorksheetNotFound:
        ws = sh.add_worksheet(title="Sessoes", rows=100, cols=len(CABECALHO))
    if ws.row_values(1) != CABECALHO:
        ws.update(range_name="A1", values=[CABECALHO])
    return ws


def segredo(nome):
    """Valor de st.secrets, ou None se não houver secrets configurados (ex.: teste local)."""
    try:
        return st.secrets[nome] if nome in st.secrets else None
    except Exception:
        return None


def tem_planilha():
    return segredo("gcp_service_account") is not None and segredo("planilha_url") is not None


# ---------------------------------------------------------------- avaliação automática
def sem_acento(t):
    return "".join(c for c in unicodedata.normalize("NFD", str(t or "").lower()) if unicodedata.category(c) != "Mn")


def proximo(hoje, dia_semana):  # 0 = segunda ... 5 = sábado
    return hoje + timedelta(days=(dia_semana - hoje.weekday()) % 7 or 7)


def reservas(dados):
    return list((dados or {}).get("reservas") or [])


def termino(r):
    try:
        return int(str(r.get("inicio", "0"))[:2]) + int(float(r.get("duracao") or 0))
    except ValueError:
        return 99


def numero(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return -1


def avaliar(i, reg, regs):
    """Resultado automático da tarefa i: Sucesso, Falha ou Revisar (quando só a responsável pode decidir)."""
    if reg.get("desistiu") or reg["tempo_s"] > LIMITE_S:
        return "Falha"
    final = reservas(reg.get("dados_fim"))
    # reservas criadas durante a tarefa (as de exemplo têm código "s0", "s1"...)
    novas = [r for r in final if r.get("id") not in reg.get("ids_inicio", []) and not str(r.get("id")).startswith("s")]
    hoje = date.fromisoformat((reg.get("dados_fim") or {}).get("hoje") or date.today().isoformat())
    txt = sem_acento(reg.get("resposta"))

    if i == 0:
        quinta = proximo(hoje, 3).isoformat()
        for r in novas:
            if (r.get("lab") == "Lab 201" and r.get("data") == quinta and r.get("inicio") == "10:00"
                    and numero(r.get("duracao")) == 2 and numero(r.get("alunos")) == 30):
                reg["id_reserva"] = r.get("id")
                return "Sucesso"
        if novas:
            reg["id_reserva"] = novas[-1].get("id")
        return "Falha"
    if i == 1:
        tem_prof, tem_hora = "danilo" in txt, bool(re.search(r"(^|\D)0?8(\D|$)", txt))
        return "Sucesso" if tem_prof and tem_hora else ("Revisar" if tem_prof or tem_hora else "Falha")
    if i == 2:
        sabado = proximo(hoje, 5)
        if not novas:
            return "Revisar" if txt else "Falha"
        for r in novas:
            try:
                d = date.fromisoformat(r.get("data"))
            except (TypeError, ValueError):
                continue
            fere = ((r.get("lab") == "Lab 202" and numero(r.get("alunos")) > 30) or numero(r.get("alunos")) > 40
                    or (d.weekday() == 5 and termino(r) > 12) or termino(r) > 22 or d.weekday() == 6)
            if fere and r.get("status") != "Cancelada":
                return "Falha"
        if any(r.get("data") == sabado.isoformat() and numero(r.get("alunos")) >= 35 for r in novas):
            return "Sucesso"
        return "Revisar"
    if i == 3:
        alvo = regs[0].get("id_reserva")
        if not alvo:
            achadas = [r for r in reservas(regs[0].get("dados_fim")) if "ana" in sem_acento(r.get("professor"))
                       and "estrutura" in sem_acento(r.get("disciplina"))]
            alvo = achadas[-1].get("id") if achadas else None
        if not alvo:
            return "Revisar"
        r = next((r for r in final if r.get("id") == alvo), None)
        return "Sucesso" if r and r.get("status") == "Cancelada" else "Falha"
    if i == 4:
        lab, hora = "101" in txt, "19" in txt
        return "Sucesso" if lab and hora else ("Revisar" if lab or hora else "Falha")
    return "Revisar"


def nota_sus(resp):
    return sum((v - 1) if q % 2 == 0 else (5 - v) for q, v in enumerate(resp)) * 2.5


# ---------------------------------------------------------------- painel da responsável
def painel():
    st.title("Resultados do teste")
    senha = segredo("senha_admin")
    if not senha or not tem_planilha():
        st.error("Configure `senha_admin`, `planilha_url` e `gcp_service_account` nos secrets do app.")
        return
    if st.text_input("Senha", type="password") != senha:
        st.stop()
    import pandas as pd
    linhas = aba_sessoes().get_all_records()
    if not linhas:
        st.info("Nenhuma sessão registrada ainda.")
        return
    df = pd.DataFrame(linhas)
    st.write(f"**{len(df)} sessões registradas.**")
    st.dataframe(df[["data_hora", "nome", "aparelho", "sus_nota"] + [f"t{n}_resultado" for n in range(1, 6)]],
                 hide_index=True)

    c1, c2 = st.columns(2)
    notas = pd.to_numeric(df["sus_nota"], errors="coerce")
    c1.metric("Nota SUS média", f"{notas.mean():.1f}".replace(".", ","))
    tot = sum((df[f"t{n}_resultado"] == "Sucesso").sum() for n in range(1, 6))
    c2.metric("Taxa de sucesso geral", f"{tot / (5 * len(df)):.0%}")
    resumo = pd.DataFrame({
        "Tarefa": [f"{n} · {TAREFAS[n - 1]['titulo']}" for n in range(1, 6)],
        "Sucesso": [(df[f"t{n}_resultado"] == "Sucesso").mean() for n in range(1, 6)],
        "Revisar": [(df[f"t{n}_resultado"] == "Revisar").sum() for n in range(1, 6)],
        "Tempo médio (s)": [pd.to_numeric(df[f"t{n}_tempo_s"], errors="coerce").mean() for n in range(1, 6)],
        "Erros": [pd.to_numeric(df[f"t{n}_erros"], errors="coerce").sum() for n in range(1, 6)],
    })
    st.dataframe(resumo, hide_index=True, column_config={"Sucesso": st.column_config.ProgressColumn(
        format="percent", min_value=0, max_value=1)})
    st.caption("“Revisar” = a tarefa precisa da sua leitura (veja as respostas e comentários na planilha do Google).")

    st.subheader("Dificuldades marcadas pelos participantes")
    contagem = pd.DataFrame(
        {f"T{n}": [sum(d in str(x).split("; ") for x in df[f"t{n}_dificuldades"]) for d in DIFICULDADES]
         for n in range(1, 6)}, index=DIFICULDADES)
    contagem["Total"] = contagem.sum(axis=1)
    st.dataframe(contagem.sort_values("Total", ascending=False))
    st.caption("Número de participantes que marcaram cada opção em cada tarefa.")

    st.subheader("Exportar para a planilha do kit")
    escolha = st.multiselect("Sessões (até 5, uma por participante)", list(range(len(df))),
                             default=list(range(min(5, len(df)))),
                             format_func=lambda k: f"{df.loc[k, 'nome']} · {df.loc[k, 'data_hora']}",
                             max_selections=5)
    if escolha:
        st.write("Na planilha exportada, os nomes viram códigos (o artigo não mostra nomes):")
        st.dataframe(pd.DataFrame({"Código": [f"P{k + 1}" for k in range(len(escolha))],
                                   "Nome": [df.loc[k, "nome"] for k in escolha]}), hide_index=True)
        st.download_button("Baixar planilha preenchida (.xlsx)", exportar(df.loc[escolha]),
                           file_name="Planilha do teste de usabilidade (colegas).xlsx")


def exportar(df):
    """Preenche a planilha do kit (abas SUS e Tarefas) com as sessões escolhidas."""
    from openpyxl import load_workbook
    from openpyxl.comments import Comment
    wb = load_workbook(AQUI / "modelo_planilha.xlsx")
    su, ta = wb["SUS"], wb["Tarefas"]
    for k, (_, s) in enumerate(df.iterrows()):
        su.cell(row=4 + k, column=1, value=f"P{k + 1}")  # sem nomes na planilha que vai para o artigo
        ta.cell(row=5 + k, column=1, value=f"P{k + 1}")
        for q in range(10):
            su.cell(row=4 + k, column=2 + q, value=int(s[f"sus_q{q + 1}"]))
        for t in range(5):
            res = s[f"t{t + 1}_resultado"]
            c = ta.cell(row=5 + k, column=2 + 3 * t, value=res if res != "Revisar" else None)
            if res == "Revisar":
                c.comment = Comment("Revisar: leia a resposta e o comentário do participante na planilha do Google.",
                                    "app")
            ta.cell(row=5 + k, column=3 + 3 * t, value=int(s[f"t{t + 1}_tempo_s"]))
            ta.cell(row=5 + k, column=4 + 3 * t, value=int(s[f"t{t + 1}_erros"]))
    buf = io.BytesIO()
    wb.save(buf)
    return buf.getvalue()


# ---------------------------------------------------------------- fluxo do participante
def estado():
    s = st.session_state
    s.setdefault("etapa", "inicio")
    s.setdefault("sessao", uuid.uuid4().hex[:12])
    s.setdefault("t", 0)
    s.setdefault("regs", [{} for _ in TAREFAS])
    s.setdefault("ultimo", None)
    return s


def mostrar_sistema(s):
    valor = sistema(sessao=s.sessao, key="sistema", default=None)
    if valor:
        s.ultimo = valor


def inicio(s):
    st.title("Teste de usabilidade")
    st.write("**Sistema de reserva de laboratórios da faculdade**")
    st.markdown(
        "Obrigado por participar! Este teste faz parte de um artigo da disciplina **Laboratório de Engenharia de "
        "Software** (Universidade Tiradentes). **Quem está sendo avaliado é o sistema, não você**: se algo der "
        "errado, é um problema do sistema, e isso ajuda muito a pesquisa.")
    with st.expander("Termo de consentimento (leia antes de começar)", expanded=True):
        st.markdown(
            "- **Responsável:** Wilia Francisco da Silva (wilia.francisco@souunit.com.br).\n"
            "- **Objetivo:** avaliar se o sistema é fácil de usar.\n"
            "- **Como funciona:** você fará 5 tarefas curtas no sistema, que aparece nesta mesma página, e no fim "
            "responderá a 10 afirmações. Leva cerca de 15 a 20 minutos. O app registra o tempo de cada tarefa, o que "
            "você fez no sistema, suas respostas e seus comentários.\n"
            "- A participação é **voluntária**, sem custo nem pagamento, e você pode desistir a qualquer momento "
            "(é só fechar a página).\n"
            "- Seu nome é pedido só para a responsável organizar as respostas. Ele **não aparecerá no artigo**: "
            "lá você será identificado apenas por um código (P1 a P5).\n"
            "- Os dados serão usados **somente neste trabalho acadêmico**. Não há gravação de áudio, vídeo nem da "
            "câmera.")
    nome = st.text_input("Seu nome", max_chars=80).strip()
    aparelho = st.radio("Em que aparelho você está fazendo o teste?", ["Celular", "Computador", "Tablet"], index=None,
                        horizontal=True)
    if aparelho and aparelho != "Celular":
        st.warning("O teste foi pensado para o **celular**. Se puder, abra este link no celular.")
    ja = st.radio("Você já reservou laboratório ou sala por algum sistema?", ["Sim", "Não"], index=None,
                  horizontal=True)
    aceito = st.checkbox("Li o termo acima e concordo em participar.")
    if st.button("Começar", type="primary", disabled=not (len(nome) >= 2 and aparelho and ja and aceito)):
        s.update(nome=nome, aparelho=aparelho, ja=ja, aceite=datetime.now().isoformat(timespec="seconds"),
                 etapa="instrucoes")
        st.rerun()


def instrucoes(s):
    st.title("Como vai funcionar")
    st.markdown(
        "1. Imagine que você é **professor(a) da faculdade** e precisa usar o sistema de reservas.\n"
        "2. Para cada tarefa, leia o cartão e toque em **Começar a tarefa**. O sistema aparece logo abaixo.\n"
        "3. **O cartão da tarefa fica preso no topo da tela** enquanto você rola o sistema, então não precisa "
        "decorar nada. Quando a tarefa pede uma resposta, o campo para escrever também fica no cartão.\n"
        "4. Faça a tarefa **sozinho(a)**, do jeito que você faria de verdade. Não existe resposta errada da sua parte.\n"
        "5. Quando terminar, toque em **Terminei** (no cartão). Se não conseguir, toque em **Não consegui**. "
        "Cada tarefa tem até **5 minutos**.\n"
        "6. Depois de cada tarefa, conte em poucas palavras o que achou: **o que estranhou, o que esperava, o que "
        "atrapalhou**. Esses comentários são a parte mais importante do teste!")
    c1, c2 = st.columns(2)
    if c1.button("Voltar", use_container_width=True):
        s.etapa = "inicio"
        st.rerun()
    if c2.button("Ir para a tarefa 1", type="primary", use_container_width=True):
        s.etapa = "tarefa"
        st.rerun()


def tarefa(s):
    i, reg = s.t, s.regs[s.t]
    if "inicio" not in reg:
        st.progress(i / len(TAREFAS), text=f"Tarefa {i + 1} de {len(TAREFAS)}")
        st.subheader(f"Tarefa {i + 1} · {TAREFAS[i]['titulo']}")
        st.info(TAREFAS[i]["texto"])
        st.caption("O tempo começa a contar quando você tocar no botão. O cartão continua visível durante a tarefa.")
        if st.button("Começar a tarefa", type="primary"):
            reg["inicio"] = time.time()
            reg["ids_inicio"] = [r.get("id") for r in reservas(s.ultimo)]
            reg["erros_inicio"] = (s.ultimo or {}).get("erros", 0)
            st.rerun()
        return
    # cartão preso no topo: a tarefa, a resposta (se houver) e os botões ficam sempre à vista
    with st.container(key="cartao"):
        st.markdown(f"**Tarefa {i + 1} de {len(TAREFAS)} · {TAREFAS[i]['titulo']}**")
        st.info(TAREFAS[i]["texto"])
        resposta = ""
        if TAREFAS[i].get("na_tarefa"):
            resposta = st.text_input(TAREFAS[i]["pergunta"], key=f"resp{i}",
                                     placeholder="Escreva aqui. Se não encontrar, escreva “não encontrei”.").strip()
        c1, c2 = st.columns(2)
        fim = c1.button("Terminei", type="primary", use_container_width=True,
                        disabled=bool(TAREFAS[i].get("na_tarefa")) and not resposta)
        desisto = c2.button("Não consegui", use_container_width=True)
    mostrar_sistema(s)
    if fim or desisto:
        reg.update(fim=time.time(), desistiu=bool(desisto), dados_fim=s.ultimo)
        if TAREFAS[i].get("na_tarefa"):
            reg["resposta"] = resposta
        reg["tempo_s"] = round(reg["fim"] - reg["inicio"])
        reg["erros"] = max(0, (s.ultimo or {}).get("erros", 0) - reg["erros_inicio"])
        s.etapa = "pos"
        st.rerun()


def pos_tarefa(s):
    i, reg = s.t, s.regs[s.t]
    st.subheader(f"Tarefa {i + 1} · sua opinião")
    st.caption("A tarefa era:")
    st.info(TAREFAS[i]["texto"])
    if TAREFAS[i].get("na_tarefa"):
        st.write(f"**Sua resposta:** {reg.get('resposta') or '—'}")
    pergunta = TAREFAS[i]["pergunta"] if not TAREFAS[i].get("na_tarefa") else None
    resposta = st.text_area(pergunta, key=f"resp{i}") if pergunta else ""
    st.write("**Como foi esta tarefa para você?** Marque tudo o que aconteceu:")
    marcadas = [d for k, d in enumerate(DIFICULDADES) if st.checkbox(d, key=f"dif{i}_{k}")]
    conflito = DIFICULDADES[0] in marcadas and len(marcadas) > 1
    if conflito:
        st.warning("Você marcou “Não tive dificuldade” junto com uma dificuldade. Desmarque uma das opções.")
    elif not marcadas:
        st.caption("Marque pelo menos uma opção para continuar.")
    comentario = st.text_area("Quer contar mais alguma coisa? O que estranhou ou esperava? (opcional)",
                              key=f"com{i}")
    if st.button("Continuar", type="primary", disabled=not marcadas or conflito):
        if pergunta:
            reg["resposta"] = resposta.strip()
        reg["dificuldades"] = marcadas
        reg["comentario"] = comentario.strip()
        reg["resultado"] = avaliar(i, reg, s.regs)
        s.t += 1
        s.etapa = "tarefa" if s.t < len(TAREFAS) else "sus"
        st.rerun()


def questionario(s):
    st.title("Questionário final")
    st.write("Pensando no sistema de reservas que você acabou de usar, marque **um número** em cada frase. "
             "Responda rápido, sem pensar muito. Se não souber responder, marque o 3.")
    st.caption("1 = discordo totalmente · 5 = concordo totalmente")
    resp = [st.radio(f"**{q + 1}.** {txt}", [1, 2, 3, 4, 5], index=None, horizontal=True, key=f"sus{q}")
            for q, txt in enumerate(SUS)]
    facil = st.text_area("O que você achou mais fácil?")
    atrapalhou = st.text_area("O que mais atrapalhou?")
    if st.button("Enviar respostas", type="primary", disabled=None in resp):
        s.sus, s.facil, s.atrapalhou = resp, facil.strip(), atrapalhou.strip()
        s.linha = montar_linha(s)
        s.salvo = salvar(s.linha)
        s.etapa = "fim"
        st.rerun()


def montar_linha(s):
    linha = [datetime.now().isoformat(timespec="seconds"), s.nome, s.aparelho, s.ja, s.sessao]
    for reg in s.regs:
        linha += [reg.get("resultado"), reg.get("tempo_s"), reg.get("erros"), reg.get("resposta", ""),
                  "; ".join(reg.get("dificuldades", [])), reg.get("comentario", "")]
    final = reservas(s.regs[-1].get("dados_fim"))
    return linha + list(s.sus) + [nota_sus(s.sus), s.facil, s.atrapalhou, json.dumps(final, ensure_ascii=False)]


def salvar(linha):
    if not tem_planilha():
        return False
    try:
        aba_sessoes().append_row(linha, value_input_option="RAW")
        return True
    except Exception as erro:  # mostra o problema, mas não perde as respostas
        st.session_state.erro_salvar = str(erro)
        return False


def fim(s):
    st.balloons()
    st.title("Obrigado! 🎉")
    st.write("Suas respostas foram registradas. Você já pode fechar esta página.")
    if not s.get("salvo"):
        st.warning("Não foi possível enviar para a planilha. Baixe o arquivo abaixo e envie para a responsável.")
        if s.get("erro_salvar"):
            st.caption(s.erro_salvar)
        st.download_button("Baixar minhas respostas", json.dumps(dict(zip(CABECALHO, s.linha)), ensure_ascii=False,
                                                                indent=2),
                           file_name=f"respostas-{s.sessao}.json")


if st.query_params.get("admin") == "1":
    painel()
else:
    s = estado()
    {"inicio": inicio, "instrucoes": instrucoes, "tarefa": tarefa, "pos": pos_tarefa, "sus": questionario,
     "fim": fim}[s.etapa](s)
