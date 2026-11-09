"""Gera componente_sistema/index.html a partir do Laboratório de Sistemas.

O arquivo do professor é copiado sem alterar as regras nem os defeitos. Só são
acrescentados, no <head>:
  - abertura direta no caso 15 e bloqueio da volta para a lista de casos;
  - comunicação com o Streamlit (protocolo de componentes): a cada gravação,
    o app recebe as reservas, o número de vezes que apareceram mensagens de
    erro do formulário e a data de "hoje" no aparelho do participante;
  - limpeza dos dados quando começa uma sessão nova (cada participante parte
    dos mesmos dados de exemplo).

Uso: python gerar_componente.py "<caminho do laboratorio-de-sistemas.html>"
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
origem = sys.argv[1]
html = open(origem, encoding="utf-8").read()

INJETADO = r"""
<style>
  .back { display: none !important; }
</style>
<script>
(function () {
  var CHAVE = "labsis:v2:caso-15";
  var SESSAO = "app-teste:sessao";
  var erros = 0, liberado = false;
  if (location.hash !== "#caso-15") history.replaceState(null, "", "#caso-15");

  function avisar(tipo, extra) {
    var m = { isStreamlitMessage: true, type: tipo };
    for (var k in (extra || {})) m[k] = extra[k];
    window.parent.postMessage(m, "*");
  }
  function hoje() {
    var d = new Date(), p = function (n) { return String(n).padStart(2, "0"); };
    return d.getFullYear() + "-" + p(d.getMonth() + 1) + "-" + p(d.getDate());
  }
  function altura() {
    avisar("streamlit:setFrameHeight", { height: Math.max(document.documentElement.scrollHeight, 600) });
  }
  function enviar() {
    if (!liberado) return;
    var reservas = null;
    try { reservas = JSON.parse(localStorage.getItem(CHAVE)); } catch (e) {}
    avisar("streamlit:setComponentValue", {
      value: { reservas: reservas, erros: erros, hoje: hoje(), t: Date.now() }, dataType: "json"
    });
  }

  // Toda gravação do caso 15 é repassada ao app.
  var gravar = Storage.prototype.setItem;
  Storage.prototype.setItem = function (k, v) {
    gravar.apply(this, arguments);
    if (k === CHAVE) setTimeout(enviar, 0);
  };

  // O app manda um código de sessão; se mudou, os dados voltam ao exemplo.
  window.addEventListener("message", function (ev) {
    var d = ev.data;
    if (!d || d.type !== "streamlit:render") return;
    var sessao = (d.args || {}).sessao, atual = null;
    try { atual = localStorage.getItem(SESSAO); } catch (e) {}
    if (sessao && atual !== sessao) {
      try { localStorage.removeItem(CHAVE); gravar.call(localStorage, SESSAO, sessao); } catch (e) {}
      location.reload();
      return;
    }
    liberado = true;
    altura();
    enviar();
  });

  document.addEventListener("DOMContentLoaded", function () {
    avisar("streamlit:componentReady", { apiVersion: 1 });
    window.addEventListener("hashchange", function () {
      if (location.hash !== "#caso-15") location.hash = "#caso-15";
    });
    // Conta cada tentativa de registrar que terminou com mensagem de erro.
    document.addEventListener("submit", function () {
      setTimeout(function () {
        var e = document.getElementById("errs");
        if (e && !e.hidden) { erros++; enviar(); }
      }, 0);
    }, true);
    new MutationObserver(altura).observe(document.body, { subtree: true, childList: true });
  });
})();
</script>
"""

saida = html.replace("</head>", INJETADO + "\n</head>", 1)
assert saida != html, "não achei </head> no arquivo do laboratório"
os.makedirs(os.path.join(AQUI, "componente_sistema"), exist_ok=True)
open(os.path.join(AQUI, "componente_sistema", "index.html"), "w", encoding="utf-8").write(saida)
print("componente gerado:", os.path.join(AQUI, "componente_sistema", "index.html"))
