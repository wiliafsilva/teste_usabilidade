"""Monta .streamlit/secrets.toml a partir da chave JSON da conta de serviço do Google.

Uso:
  python gerar_secrets.py <chave.json> <link da planilha> <senha do painel>

O arquivo gerado fica em .streamlit/secrets.toml (já está no .gitignore, não vai
para o GitHub). O mesmo conteúdo é o que se cola em Settings > Secrets no
Streamlit Cloud. O script não mostra a chave privada na tela.
"""
import json
import sys
from pathlib import Path

chave, url, senha = sys.argv[1], sys.argv[2], sys.argv[3]
dados = json.loads(Path(chave).read_text(encoding="utf-8"))
if dados.get("type") != "service_account":
    sys.exit("Este arquivo não é uma chave de conta de serviço (campo type diferente de service_account).")
if "docs.google.com/spreadsheets/d/" not in url:
    sys.exit("O link não parece ser de uma planilha do Google (docs.google.com/spreadsheets/d/...).")

linhas = [f"senha_admin = {json.dumps(senha)}", f"planilha_url = {json.dumps(url)}", "", "[gcp_service_account]"]
linhas += [f"{k} = {json.dumps(v)}" for k, v in dados.items()]
destino = Path(__file__).parent / ".streamlit" / "secrets.toml"
destino.parent.mkdir(exist_ok=True)
destino.write_text("\n".join(linhas) + "\n", encoding="utf-8")
print("secrets gerado em:", destino)
print("Compartilhe a planilha, como Editor, com:", dados["client_email"])
