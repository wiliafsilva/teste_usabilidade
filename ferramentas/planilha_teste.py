"""Gera a planilha do teste de usabilidade (SUS, tarefas, problemas e resumo).

Uso: python planilha_teste.py <saida.xlsx> [--exemplo]
  --exemplo  preenche P1 a P5 com dados fictícios (só para conferir as fórmulas).
As células amarelas são as que se preenchem; todo o resto é calculado.
"""
import sys

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter as col
from openpyxl.worksheet.datavalidation import DataValidation

saida = sys.argv[1]
EXEMPLO = "--exemplo" in sys.argv

FONTE = "Arial"
AMARELO = PatternFill("solid", start_color="FFF2CC")
CINZA = PatternFill("solid", start_color="E7E6E6")
AZUL = PatternFill("solid", start_color="DDEBF7")
fino = Side(style="thin", color="999999")
BORDA = Border(left=fino, right=fino, top=fino, bottom=fino)
PART = ["P1", "P2", "P3", "P4", "P5"]
TAREFAS = [
    "1 · Reservar o Lab 201 (quinta, 10h às 12h)",
    "2 · Achar a primeira reserva do Lab 101",
    "3 · Reservar no sábado, 35 alunos, 10h às 13h",
    "4 · Cancelar a reserva da tarefa 1",
    "5 · Buscar a aula de Banco de Dados",
]
SUS = [
    "Gostaria de usar este sistema com frequência.",
    "Achei o sistema desnecessariamente complexo.",
    "Achei o sistema fácil de usar.",
    "Precisaria de ajuda técnica para usar o sistema.",
    "As funções do sistema estão bem integradas.",
    "Há muita inconsistência no sistema.",
    "A maioria das pessoas aprenderia a usar rapidamente.",
    "Achei o sistema muito complicado de usar.",
    "Me senti muito confiante usando o sistema.",
    "Precisei aprender muitas coisas antes de usar.",
]
HEURISTICAS = [
    "Diálogo simples e natural", "Falar a língua do usuário", "Minimizar a carga de memória",
    "Ser consistente", "Fornecer feedback", "Saídas claramente marcadas", "Oferecer atalhos",
    "Boas mensagens de erro", "Prevenir erros",
]


def celula(ws, ref, valor=None, negrito=False, preencher=None, centro=False, fmt=None, quebra=False, tam=10,
           italico=False, cor="000000"):
    c = ws[ref]
    if valor is not None:
        c.value = valor
    c.font = Font(name=FONTE, bold=negrito, size=tam, italic=italico, color=cor)
    if preencher:
        c.fill = preencher
    c.alignment = Alignment(horizontal="center" if centro else None, vertical="center", wrap_text=quebra)
    if fmt:
        c.number_format = fmt
    return c


def grade(ws, intervalo):
    for linha in ws[intervalo]:
        for c in linha:
            c.border = BORDA


wb = Workbook()

# ------------------------------------------------------------------ Listas (oculta)
ls = wb.create_sheet("Listas")
for k, v in enumerate(["Sucesso", "Sucesso com ajuda", "Falha"], 1):
    ls.cell(row=k, column=1, value=v)
for k, v in enumerate(HEURISTICAS, 1):
    ls.cell(row=k, column=2, value=v)
for k, v in enumerate(["Alto", "Médio", "Baixo"], 1):
    ls.cell(row=k, column=3, value=v)
ls.sheet_state = "hidden"

# ------------------------------------------------------------------ Como usar
cu = wb.active
cu.title = "Como usar"
cu.column_dimensions["A"].width = 4
cu.column_dimensions["B"].width = 100
celula(cu, "B2", "Planilha do teste de usabilidade · Sistema de reserva de laboratórios (Caso 15)", negrito=True, tam=14)
celula(cu, "B3", "Responsável: Wilia Francisco da Silva · Artigo, Tema 6", italico=True)
linhas = [
    ("Legenda", True, None),
    ("Células amarelas: preencha. Todas as outras são calculadas sozinhas; não digite nelas.", False, AMARELO),
    ("Células azuis: resultados que vão para o artigo.", False, AZUL),
    ("", False, None),
    ("Passo a passo", True, None),
    ("1. Aba SUS: digite a resposta (1 a 5) de cada participante para as 10 afirmações. A nota de 0 a 100 aparece "
     "quando as 10 respostas estiverem preenchidas.", False, None),
    ("2. Aba Tarefas: para cada participante e tarefa, escolha o resultado na lista, digite o tempo em SEGUNDOS "
     "(ex.: 2 min 35 s = 155) e o número de erros.", False, None),
    ("3. Aba Problemas: uma linha por problema observado. Escolha a heurística e o impacto nas listas e escreva "
     "a melhoria proposta.", False, None),
    ("4. Aba Resumo: confira os números finais (taxa de sucesso, tempo médio, nota SUS e problemas por impacto).",
     False, None),
    ("", False, None),
    ("Como a nota SUS é calculada (BROOKE, 1996)", True, None),
    ("Itens ímpares: resposta − 1. Itens pares: 5 − resposta. A soma dos 10 valores × 2,5 dá a nota de 0 a 100.",
     False, None),
    ("Faixas de aceitabilidade (BANGOR; KORTUM; MILLER, 2008): abaixo de 50 = Inaceitável; de 50 a 70 = Marginal; "
     "acima de 70 = Aceitável.", False, None),
    ("", False, None),
    ("Cada aba tem, no fim, uma linha de EXEMPLO em cinza que mostra o formato esperado. Ela não entra nos cálculos.",
     False, None),
]
for k, (txt, neg, fill) in enumerate(linhas, 5):
    celula(cu, f"B{k}", txt, negrito=neg, preencher=fill, quebra=True)

# ------------------------------------------------------------------ SUS
su = wb.create_sheet("SUS")
celula(su, "A1", "Questionário SUS: respostas de 1 (discordo totalmente) a 5 (concordo totalmente)", negrito=True, tam=12)
su["A3"] = "Participante"
for q in range(10):
    su.cell(row=3, column=2 + q, value=f"Q{q + 1}")
    su.cell(row=3, column=2 + q).comment = Comment(SUS[q], "Kit")
su["L3"], su["M3"] = "Nota SUS (0 a 100)", "Faixa"
for ref in ["A3", "L3", "M3"] + [f"{col(2 + q)}3" for q in range(10)]:
    celula(su, ref, negrito=True, preencher=CINZA, centro=True, quebra=True)
dv15 = DataValidation(type="whole", operator="between", formula1="1", formula2="5", allow_blank=True,
                      showErrorMessage=True, errorTitle="Valor inválido", error="Digite um número inteiro de 1 a 5.")
su.add_data_validation(dv15)
for i, p in enumerate(PART):
    r = 4 + i
    celula(su, f"A{r}", p, negrito=True, centro=True)
    for q in range(10):
        ref = f"{col(2 + q)}{r}"
        celula(su, ref, preencher=AMARELO, centro=True)
        dv15.add(ref)
    termos = "+".join(f"({col(2 + q)}{r}-1)" if q % 2 == 0 else f"(5-{col(2 + q)}{r})" for q in range(10))
    celula(su, f"L{r}", f'=IF(COUNT(B{r}:K{r})<10,"",({termos})*2.5)', centro=True, fmt="0.0")
    celula(su, f"M{r}", f'=IF(L{r}="","",IF(L{r}<50,"Inaceitável",IF(L{r}<=70,"Marginal","Aceitável")))', centro=True)
celula(su, "A9", "Média", negrito=True, centro=True, preencher=CINZA)
celula(su, "L9", '=IFERROR(AVERAGE(L4:L8),"")', negrito=True, centro=True, fmt="0.0", preencher=AZUL)
celula(su, "M9", '=IF(L9="","",IF(L9<50,"Inaceitável",IF(L9<=70,"Marginal","Aceitável")))', negrito=True,
       centro=True, preencher=AZUL)
celula(su, "K9", "Respostas completas:", centro=False, tam=9)
celula(su, "K10", '=COUNT(L4:L8)', centro=True)
grade(su, "A3:M9")
# exemplo
celula(su, "A12", "EXEMPLO (não entra no cálculo)", italico=True, cor="808080", tam=9)
ex = [4, 2, 4, 1, 4, 2, 5, 2, 4, 2]
celula(su, "A13", "P0", italico=True, cor="808080", centro=True, preencher=CINZA)
for q, v in enumerate(ex):
    celula(su, f"{col(2 + q)}13", v, italico=True, cor="808080", centro=True, preencher=CINZA)
celula(su, "L13", "80,0", italico=True, cor="808080", centro=True, preencher=CINZA)
celula(su, "M13", "Aceitável", italico=True, cor="808080", centro=True, preencher=CINZA)
celula(su, "A15", "Afirmações", negrito=True)
for q, txt in enumerate(SUS):
    celula(su, f"A{16 + q}", f"Q{q + 1}", centro=True)
    su.merge_cells(f"B{16 + q}:M{16 + q}")
    celula(su, f"B{16 + q}", txt)
su.column_dimensions["A"].width = 14
for q in range(10):
    su.column_dimensions[col(2 + q)].width = 6
su.column_dimensions["L"].width = 12
su.column_dimensions["M"].width = 13
su.row_dimensions[3].height = 30
su.freeze_panes = "B4"

# ------------------------------------------------------------------ Tarefas
ta = wb.create_sheet("Tarefas")
celula(ta, "A1", "Resultado de cada tarefa · tempo em SEGUNDOS (limite: 300 s = 5 min)", negrito=True, tam=12)
celula(ta, "A3", "Participante", negrito=True, preencher=CINZA, centro=True, quebra=True)
ta.merge_cells("A3:A4")
dv_res = DataValidation(type="list", formula1="=Listas!$A$1:$A$3", allow_blank=True, showErrorMessage=True,
                        error="Escolha Sucesso, Sucesso com ajuda ou Falha.")
dv_num = DataValidation(type="whole", operator="between", formula1="0", formula2="3600", allow_blank=True,
                        showErrorMessage=True, error="Digite um número inteiro (segundos ou erros).")
ta.add_data_validation(dv_res)
ta.add_data_validation(dv_num)
for t in range(5):
    c0 = 2 + 3 * t
    a, b, c = col(c0), col(c0 + 1), col(c0 + 2)
    ta.merge_cells(f"{a}3:{c}3")
    celula(ta, f"{a}3", TAREFAS[t], negrito=True, preencher=CINZA, centro=True, quebra=True)
    for ref, txt in [(f"{a}4", "Resultado"), (f"{b}4", "Tempo (s)"), (f"{c}4", "Erros")]:
        celula(ta, ref, txt, negrito=True, preencher=CINZA, centro=True)
    for i in range(5):
        r = 5 + i
        for ref in (f"{a}{r}", f"{b}{r}", f"{c}{r}"):
            celula(ta, ref, preencher=AMARELO, centro=True)
        dv_res.add(f"{a}{r}")
        dv_num.add(f"{b}{r}")
        dv_num.add(f"{c}{r}")
    # linhas de resumo da tarefa
    celula(ta, f"{a}11", f'=IF(COUNTA({a}5:{a}9)=0,"",COUNTIF({a}5:{a}9,"Sucesso")/COUNTA({a}5:{a}9))',
           centro=True, fmt="0%", preencher=AZUL)
    celula(ta, f"{a}12", f'=IF(COUNTA({a}5:{a}9)=0,"",(COUNTIF({a}5:{a}9,"Sucesso")+COUNTIF({a}5:{a}9,'
                         f'"Sucesso com ajuda"))/COUNTA({a}5:{a}9))', centro=True, fmt="0%")
    celula(ta, f"{b}13", f'=IFERROR(AVERAGE({b}5:{b}9),"")', centro=True, fmt="0", preencher=AZUL)
    celula(ta, f"{b}14", f'=IFERROR(AVERAGEIF({a}5:{a}9,"Sucesso",{b}5:{b}9),"")', centro=True, fmt="0")
    celula(ta, f"{c}15", f'=SUM({c}5:{c}9)', centro=True, preencher=AZUL)
for i, p in enumerate(PART):
    celula(ta, f"A{5 + i}", p, negrito=True, centro=True)
for r, txt in [(11, "Taxa de sucesso (sem ajuda)"), (12, "Sucesso com ou sem ajuda"), (13, "Tempo médio (s)"),
               (14, "Tempo médio de quem teve sucesso (s)"), (15, "Total de erros")]:
    celula(ta, f"A{r}", txt, negrito=True, preencher=CINZA, quebra=True, tam=9)
grade(ta, "A3:P9")
grade(ta, "A11:P15")
celula(ta, "A17", "EXEMPLO (não entra no cálculo)", italico=True, cor="808080", tam=9)
for ref, v in [("A18", "P0"), ("B18", "Sucesso"), ("C18", 95), ("D18", 1), ("E18", "Sucesso com ajuda"),
               ("F18", 210), ("G18", 3), ("H18", "Falha"), ("I18", 300), ("J18", 4)]:
    celula(ta, ref, v, italico=True, cor="808080", centro=True, preencher=CINZA)
ta.column_dimensions["A"].width = 20
for t in range(5):
    ta.column_dimensions[col(2 + 3 * t)].width = 17
    ta.column_dimensions[col(3 + 3 * t)].width = 9
    ta.column_dimensions[col(4 + 3 * t)].width = 7
ta.row_dimensions[3].height = 42
ta.freeze_panes = "B5"

# ------------------------------------------------------------------ Problemas
pr = wb.create_sheet("Problemas")
celula(pr, "A1", "Problemas de usabilidade observados (uma linha por problema)", negrito=True, tam=12)
cab = ["Nº", "Tarefa", "O que aconteceu", "Participantes afetados (nº)", "Heurística", "Impacto",
       "Melhoria proposta (versão 2.0)", "Defeito relacionado (ex.: D03)"]
larg = [6, 8, 45, 13, 26, 10, 45, 14]
for k, (h, w) in enumerate(zip(cab, larg), 1):
    celula(pr, f"{col(k)}3", h, negrito=True, preencher=CINZA, centro=True, quebra=True)
    pr.column_dimensions[col(k)].width = w
dv_heu = DataValidation(type="list", formula1="=Listas!$B$1:$B$9", allow_blank=True)
dv_imp = DataValidation(type="list", formula1="=Listas!$C$1:$C$3", allow_blank=True, showErrorMessage=True,
                        error="Escolha Alto, Médio ou Baixo.")
dv_tar = DataValidation(type="whole", operator="between", formula1="1", formula2="5", allow_blank=True)
dv_npa = DataValidation(type="whole", operator="between", formula1="1", formula2="5", allow_blank=True)
for dv in (dv_heu, dv_imp, dv_tar, dv_npa):
    pr.add_data_validation(dv)
for i in range(20):
    r = 4 + i
    celula(pr, f"A{r}", f"U{i + 1:02d}", centro=True)
    for k in range(2, 9):
        celula(pr, f"{col(k)}{r}", preencher=AMARELO, quebra=True, centro=k in (2, 4, 6, 8))
    dv_tar.add(f"B{r}")
    dv_npa.add(f"D{r}")
    dv_heu.add(f"E{r}")
    dv_imp.add(f"F{r}")
grade(pr, "A3:H23")
celula(pr, "A25", "EXEMPLO (não entra no cálculo)", italico=True, cor="808080", tam=9)
for k, v in enumerate(["U00", 5, "Buscou por \"Banco de Dados\" e a lista ficou vazia; achou que a reserva não "
                       "existia.", 3, "Fornecer feedback", "Alto", "Buscar também pela disciplina e, quando não "
                       "achar nada, mostrar \"Nenhuma reserva encontrada para ...\".", "D03"], 1):
    celula(pr, f"{col(k)}26", v, italico=True, cor="808080", preencher=CINZA, quebra=True, centro=k in (1, 2, 4, 6, 8))
pr.row_dimensions[26].height = 45
pr.freeze_panes = "A4"

# ------------------------------------------------------------------ Resumo
rs = wb.create_sheet("Resumo", 1)
celula(rs, "A1", "Resumo do teste (números para o artigo)", negrito=True, tam=12)
for k, h in enumerate(["Tarefa", "Taxa de sucesso (sem ajuda)", "Sucesso com ou sem ajuda", "Tempo médio (s)",
                       "Tempo médio de quem teve sucesso (s)", "Total de erros"], 1):
    celula(rs, f"{col(k)}3", h, negrito=True, preencher=CINZA, centro=True, quebra=True)
for t in range(5):
    r = 4 + t
    a, b, c = col(2 + 3 * t), col(3 + 3 * t), col(4 + 3 * t)
    celula(rs, f"A{r}", TAREFAS[t], quebra=True)
    celula(rs, f"B{r}", f"=Tarefas!{a}11", centro=True, fmt="0%", preencher=AZUL)
    celula(rs, f"C{r}", f"=Tarefas!{a}12", centro=True, fmt="0%")
    celula(rs, f"D{r}", f"=Tarefas!{b}13", centro=True, fmt="0", preencher=AZUL)
    celula(rs, f"E{r}", f"=Tarefas!{b}14", centro=True, fmt="0")
    celula(rs, f"F{r}", f"=Tarefas!{c}15", centro=True, preencher=AZUL)
res_cols = [col(2 + 3 * t) for t in range(5)]
suc = "+".join(f'COUNTIF(Tarefas!{a}5:{a}9,"Sucesso")' for a in res_cols)
ajuda = "+".join(f'COUNTIF(Tarefas!{a}5:{a}9,"Sucesso com ajuda")' for a in res_cols)
tot = "+".join(f"COUNTA(Tarefas!{a}5:{a}9)" for a in res_cols)
celula(rs, "A9", "Todas as tarefas", negrito=True, preencher=CINZA)
celula(rs, "B9", f'=IF(({tot})=0,"",({suc})/({tot}))', negrito=True, centro=True, fmt="0%", preencher=AZUL)
celula(rs, "C9", f'=IF(({tot})=0,"",({suc}+{ajuda})/({tot}))', negrito=True, centro=True, fmt="0%")
celula(rs, "D9", '=IFERROR(AVERAGE(D4:D8),"")', negrito=True, centro=True, fmt="0")
celula(rs, "F9", "=SUM(F4:F8)", negrito=True, centro=True)
grade(rs, "A3:F9")

celula(rs, "A11", "Questionário SUS", negrito=True, preencher=CINZA)
celula(rs, "A12", "Nota SUS média (0 a 100)")
celula(rs, "B12", "=SUS!L9", negrito=True, centro=True, fmt="0.0", preencher=AZUL)
celula(rs, "A13", "Faixa (Bangor; Kortum; Miller, 2008)")
celula(rs, "B13", "=SUS!M9", negrito=True, centro=True, preencher=AZUL)
celula(rs, "A14", "Menor nota")
celula(rs, "B14", '=IF(COUNT(SUS!L4:L8)=0,"",MIN(SUS!L4:L8))', centro=True, fmt="0.0")
celula(rs, "A15", "Maior nota")
celula(rs, "B15", '=IF(COUNT(SUS!L4:L8)=0,"",MAX(SUS!L4:L8))', centro=True, fmt="0.0")
celula(rs, "A16", "Participantes com questionário completo")
celula(rs, "B16", "=COUNT(SUS!L4:L8)", centro=True)
grade(rs, "A11:B16")

celula(rs, "A18", "Problemas encontrados", negrito=True, preencher=CINZA)
for k, imp in enumerate(["Alto", "Médio", "Baixo"]):
    celula(rs, f"A{19 + k}", f"Impacto {imp.lower()}")
    celula(rs, f"B{19 + k}", f'=COUNTIF(Problemas!F4:F23,"{imp}")', centro=True, preencher=AZUL)
celula(rs, "A22", "Total de problemas", negrito=True)
celula(rs, "B22", '=COUNTA(Problemas!C4:C23)', negrito=True, centro=True, preencher=AZUL)
grade(rs, "A18:B22")
rs.column_dimensions["A"].width = 44
for k in "BCDEF":
    rs.column_dimensions[k].width = 16
rs.row_dimensions[3].height = 45

# ------------------------------------------------------------------ dados de exemplo (só para testes)
if EXEMPLO:
    import random
    random.seed(7)
    for i in range(5):
        for q in range(10):
            su.cell(row=4 + i, column=2 + q, value=random.randint(1, 5))
        for t in range(5):
            ta.cell(row=5 + i, column=2 + 3 * t, value=random.choice(["Sucesso", "Sucesso com ajuda", "Falha"]))
            ta.cell(row=5 + i, column=3 + 3 * t, value=random.randint(40, 300))
            ta.cell(row=5 + i, column=4 + 3 * t, value=random.randint(0, 4))
    for i, imp in enumerate(["Alto", "Médio", "Alto", "Baixo"]):
        pr.cell(row=4 + i, column=3, value=f"Problema {i + 1}")
        pr.cell(row=4 + i, column=6, value=imp)

wb.save(saida)
print("planilha gerada:", saida)
