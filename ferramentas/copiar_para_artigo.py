"""Copia uma parte do artigo escrita numa entrega para o arquivo do artigo.

Uso: python copiar_para_artigo.py <entrega.tex> <secao>
  secao = fundamentacao | desenvolvimento

Na entrega, o texto fica entre o título da seção do artigo e
"\\subsection*{Referências citadas...}". No artigo, ele substitui tudo entre
"\\section{<Título>}" e o comentário que abre a seção seguinte. Os
\\subsection* da entrega viram \\subsection numeradas no artigo.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIGO = os.path.join(RAIZ, "Artigo", "Artigo_entrega", "artigo-teste-usabilidade.tex")
SECOES = {
    "fundamentacao": ("Fundamentação Teórica", "% 3. DESENVOLVIMENTO"),
    "desenvolvimento": ("Desenvolvimento", "% 4. CONSIDERAÇÕES FINAIS"),
}

entrega, secao = sys.argv[1], sys.argv[2]
titulo, proxima = SECOES[secao]

src = open(entrega, encoding="utf-8").read()
ini = src.index(r"\subsection*{", src.index(r"\section{Artigo:"))
fim = src.index(r"\subsection*{Referências citadas")
texto = src[ini:fim].strip().replace(r"\subsection*{", r"\subsection{")

art = open(ARTIGO, encoding="utf-8").read()
a = art.index(r"\section{" + titulo + "}") + len(r"\section{" + titulo + "}")
b = art.rindex("% ====", 0, art.index(proxima))
art = art[:a] + "\n\n" + texto + "\n\n" + art[b:]
open(ARTIGO, "w", encoding="utf-8").write(art)
print(f"{secao}: {len(texto)} caracteres copiados para o artigo;",
      len(re.findall(r"\\pendente\{", art)), "marcas [PENDENTE] restantes")
