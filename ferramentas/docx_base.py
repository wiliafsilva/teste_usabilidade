"""Funções comuns para gerar os .docx das entregas (mesma formatação dos .tex).

Partes de texto com formatação são listas de tuplas (texto, negrito[, itálico]).
"""
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

PROFESSOR = "Sérgio Santana"
DISCIPLINA = "Laboratório de Engenharia de Software"
INTEGRANTE = "Wilia Francisco da Silva"
REGRA = "Reservas de 1 a 4 horas, para até 40 alunos"


class Entrega:
    def __init__(self):
        self.doc = Document()
        sec = self.doc.sections[0]
        sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)
        sec.top_margin, sec.bottom_margin = Cm(3), Cm(2.5)
        sec.left_margin, sec.right_margin = Cm(3), Cm(3)
        st = self.doc.styles["Normal"]
        st.font.name = "Times New Roman"
        st.font.size = Pt(12)
        st.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
        st.paragraph_format.space_after = Pt(6)

    # ---------- texto ----------
    def par(self, texto="", bold=False, size=None, center=False, after=None, italic=False):
        p = self.doc.add_paragraph()
        if center:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if after is not None:
            p.paragraph_format.space_after = Pt(after)
        r = p.add_run(texto)
        r.bold, r.italic = bold, italic
        if size:
            r.font.size = Pt(size)
        return p

    def rico(self, partes, size=None, just=False, style=None):
        p = self.doc.add_paragraph(style=style)
        if just:
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for parte in partes:
            r = p.add_run(parte[0])
            r.bold = parte[1]
            r.italic = len(parte) > 2 and parte[2]
            if size:
                r.font.size = Pt(size)
        return p

    def secao(self, texto, size=13):
        p = self.par(texto, bold=True, size=size)
        p.paragraph_format.space_before = Pt(12)

    def lista(self, itens):
        for item in itens:
            self.doc.add_paragraph(item, style="List Bullet")

    def legenda(self, texto):
        rotulo, resto = texto.split(".", 1)
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(rotulo + ".")
        r.bold = True
        r.font.size = Pt(10)
        p.add_run(resto).font.size = Pt(10)

    def imagens(self, caminhos, largura_cm):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for k, c in enumerate(caminhos):
            if k:
                p.add_run("      ")
            p.add_run().add_picture(c, width=Cm(largura_cm))

    # ---------- tabelas ----------
    @staticmethod
    def _celula(cell, valor):
        partes = valor if isinstance(valor, list) else [(valor, False)]
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        for parte in partes:
            r = p.add_run(parte[0])
            r.bold = parte[1]
            r.italic = len(parte) > 2 and parte[2]

    def tabela(self, cabecalho, linhas, larguras, centro=()):
        t = self.doc.add_table(rows=0, cols=len(larguras))
        t.style = "Table Grid"
        if cabecalho:
            for cell, h in zip(t.add_row().cells, cabecalho):
                self._celula(cell, [(h, True)])
        for linha in linhas:
            cells = t.add_row().cells
            for i, v in enumerate(linha):
                self._celula(cells[i], v)
                if i in centro:
                    cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for row in t.rows:
            for i, w in enumerate(larguras):
                row.cells[i].width = Cm(w)
        self.doc.add_paragraph()
        return t

    # ---------- blocos fixos ----------
    def cabecalho(self, titulo):
        self.par("PROJETO DE ENGENHARIA DE SOFTWARE", bold=True, size=10, center=True, after=2)
        self.par(titulo, bold=True, size=16, center=True, after=4)
        self.par("Caso 15 · Reserva de laboratórios da faculdade", size=14, center=True, after=12)
        self.tabela(None, [
            [[("Professor", True)], PROFESSOR],
            [[("Disciplina", True)], DISCIPLINA],
            [[("Integrante", True)], INTEGRANTE],
            [[("Regra para testar", True)], REGRA],
        ], [4, 11])

    def salvar(self, caminho):
        self.doc.save(caminho)
        print("docx gerado:", caminho)


# Referências usadas nas entregas e no artigo (ABNT)
REFS = {
    "F1": [("NIELSEN, J.; LANDAUER, T. K. A mathematical model of the finding of usability problems. In: ", False),
           ("Proceedings of the INTERCHI'93 Conference on Human Factors in Computing Systems", False, True),
           (". Amsterdam: ACM, 1993. p. 206–213. DOI: 10.1145/169059.169166.", False)],
    "F2": [("NIELSEN, J.; MOLICH, R. Heuristic evaluation of user interfaces. In: ", False),
           ("Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI'90)", False, True),
           (". Seattle: ACM, 1990. p. 249–256. DOI: 10.1145/97243.97281.", False)],
    "F3": [("BROOKE, J. SUS: a “quick and dirty” usability scale. In: JORDAN, P. W. et al. (Ed.). ", False),
           ("Usability Evaluation in Industry", False, True),
           (". London: Taylor & Francis, 1996. p. 189–194.", False)],
    "F4": [("BANGOR, A.; KORTUM, P. T.; MILLER, J. T. An empirical evaluation of the System Usability Scale. ", False),
           ("International Journal of Human-Computer Interaction", False, True),
           (", v. 24, n. 6, p. 574–594, 2008. DOI: 10.1080/10447310802205776.", False)],
    "F5": [("BARBOSA, S. D. J.; SILVA, B. S. ", False), ("Interação humano-computador", False, True),
           (". Rio de Janeiro: Elsevier, 2010.", False)],
}
