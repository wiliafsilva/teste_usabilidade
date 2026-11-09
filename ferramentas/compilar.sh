#!/usr/bin/env bash
# Compila uma entrega: .tex -> .pdf (pdflatex) e gera o .docx correspondente.
# Uso: bash ferramentas/compilar.sh <numero da aula>   (ex.: bash ferramentas/compilar.sh 2)
#      As figuras em figuras/*.tex também viram .png (usados no .docx).
#      bash ferramentas/compilar.sh artigo
# O pdflatex roda numa pasta temporária, porque os nomes dos arquivos têm "·".
set -e
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
FERR="$RAIZ/ferramentas"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

compila() {  # $1 = .tex de origem, $2 = pasta de destino
  cp "$1" "$TMP/doc.tex"
  [ -d "$2/figuras" ] && cp -r "$2/figuras" "$TMP/"
  (cd "$TMP" && for i in 1 2 3; do pdflatex -interaction=nonstopmode doc.tex > log.txt 2>&1 || true; done)
  if grep -q "^!" "$TMP/log.txt"; then grep -A3 "^!" "$TMP/log.txt"; exit 1; fi
  cp "$TMP/doc.pdf" "${1%.tex}.pdf"
  grep "Output written" "$TMP/log.txt"
}

figuras_png() {  # $1 = pasta da entrega; gera figuras/<nome>.png a partir de cada figuras/<nome>.tex
  [ -d "$1/figuras" ] || return 0
  for f in "$1"/figuras/*.tex; do
    n="$(basename "$f" .tex)"
    printf '%s\n' '\documentclass[border=6pt]{standalone}' '\usepackage[utf8]{inputenc}' \
      '\usepackage[T1]{fontenc}' '\usepackage{times}' '\usepackage{amssymb}' '\usepackage{tikz}' \
      '\usetikzlibrary{arrows.meta,positioning,shapes.multipart}' '\begin{document}' \
      "\\input{figuras/$n}" '\end{document}' > "$TMP/fig-$n.tex"
    (cd "$TMP" && pdflatex -interaction=nonstopmode "fig-$n.tex" > /dev/null 2>&1 || true)
    pdftoppm -png -r 220 -singlefile "$TMP/fig-$n.pdf" "$1/figuras/$n"
  done
}

case "$1" in
  1) D="$RAIZ/Artigo/entrega/entrega-26-10-26"; N="Aula 1 · 26-10 · Entender o problema e definir o escopo"
     compila "$D/$N.tex" "$D"; python -I "$FERR/docx_aula1.py" "$D/$N.docx" ;;
  2) D="$RAIZ/Artigo/entrega/entrega-09-11-26"; N="Aula 2 · 09-11 · Planejar o trabalho"
     compila "$D/$N.tex" "$D"; python -I "$FERR/docx_aula2.py" "$D/$N.docx" ;;
  3) D="$RAIZ/Artigo/entrega/entrega-16-11-26"; N="Aula 3 · 16-11 · Desenhar as partes do sistema"
     compila "$D/$N.tex" "$D"; figuras_png "$D"; python -I "$FERR/docx_aula3.py" "$D/$N.docx" "$D/figuras" ;;
  4) D="$RAIZ/Artigo/entrega/entrega-23-11-26"; N="Aula 4 · 23-11 · Escolher a solução e organizar os dados"
     compila "$D/$N.tex" "$D"; figuras_png "$D"; python -I "$FERR/docx_aula4.py" "$D/$N.docx" "$D/figuras" ;;
  artigo) D="$RAIZ/Artigo/Artigo_entrega"; compila "$D/artigo-teste-usabilidade.tex" "$D" ;;
  kit) D="$RAIZ/Artigo/teste-usabilidade"; N="Kit do teste de usabilidade"
     compila "$D/$N.tex" "$D"; python -I "$FERR/docx_kit.py" "$D/$N.docx"
     X="$D/Planilha do teste de usabilidade.xlsx"   # nunca sobrescrever: pode ter dados digitados
     if [ -e "$X" ]; then echo "planilha mantida (já existe): $X"; else python -I "$FERR/planilha_teste.py" "$X"; fi ;;
  *) echo "Uso: $0 {1|2|3|4|artigo|kit}"; exit 1 ;;
esac
