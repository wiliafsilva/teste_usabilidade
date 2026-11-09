# Teste de usabilidade remoto · Reserva de laboratórios

App em Streamlit para aplicar, **pela internet e sem a responsável junto**, o teste de
usabilidade do sistema de reserva de laboratórios (Caso 15, versão 1.0) com 5 colegas.

**O que o participante faz:** abre o link no celular, digita o nome, aceita o
termo, faz as 5 tarefas no sistema (que aparece dentro da página), comenta cada tarefa e
responde ao questionário SUS. Leva de 15 a 20 minutos.

**O que o app registra sozinho:** o tempo de cada tarefa, quantas vezes apareceram mensagens
de erro no formulário, as reservas que a pessoa criou, cancelou ou excluiu, as respostas, os
comentários e a nota SUS. Cada tarefa recebe um resultado automático: **Sucesso**, **Falha**
ou **Revisar** (quando só você pode decidir, por exemplo se a pessoa explicou uma alternativa).

## Arquivos

| Arquivo | Para quê |
|---|---|
| `app.py` | O app (participante + painel de resultados) |
| `componente_sistema/index.html` | O sistema do professor, sem mudanças nas regras, com o código que avisa o app |
| `gerar_componente.py` | Recria o `index.html` a partir do arquivo do laboratório |
| `modelo_planilha.xlsx` | A planilha do kit, preenchida pelo botão de exportação |
| `requirements.txt` | Bibliotecas usadas |
| `.streamlit/secrets.toml.example` | Modelo dos segredos (senha, link da planilha, chave do Google) |

## 1. Testar no seu computador

```bash
cd app-teste-usabilidade
pip install -r requirements.txt
streamlit run app.py
```

Abra o endereço que aparecer (http://localhost:8501), faça as 5 tarefas e confira se:
- o sistema aparece dentro da página já no caso 15, sem o botão "Todos os casos";
- ao terminar, a tela final oferece **Baixar minhas respostas** (sem a planilha do Google
  configurada, é o comportamento esperado).

## 2. Criar a planilha do Google e a chave de acesso

1. Crie uma planilha nova no Google Sheets (por exemplo, "Teste de usabilidade · respostas").
   Copie o link dela.
2. Entre em <https://console.cloud.google.com/>, crie um projeto e ative as APIs
   **Google Sheets API** e **Google Drive API** (menu *APIs e serviços › Biblioteca*).
3. Em *APIs e serviços › Credenciais*, crie uma **conta de serviço**. Abra a conta,
   vá em *Chaves › Adicionar chave › JSON* e baixe o arquivo.
4. No arquivo baixado, copie o `client_email` e **compartilhe a planilha com esse e-mail
   como Editor** (botão Compartilhar da planilha).

O app cria sozinho a aba **Sessoes** com os cabeçalhos na primeira gravação.

## 3. Publicar no Streamlit Community Cloud (grátis)

1. Crie um repositório no GitHub e envie **esta pasta** (`app-teste-usabilidade`).
   O `.gitignore` já impede o envio de `secrets.toml` e de arquivos `.json`.
2. Entre em <https://share.streamlit.io/>, clique em **Create app**, escolha o repositório
   e o arquivo `app.py`.
3. Em **Advanced settings › Secrets**, cole o conteúdo de `.streamlit/secrets.toml.example`
   trocando pelos valores reais: a sua senha, o link da planilha e os campos do arquivo JSON
   da conta de serviço.
4. Clique em **Deploy**. O link fica parecido com `https://seu-app.streamlit.app`.

## 4. Aplicar o teste

- Envie o link para cada colega e peça que abra **no celular**, num momento tranquilo. Cada um
  digita o próprio nome; no artigo, os nomes viram P1 a P5 (veja o item 5).
- Faça você mesma uma sessão de teste antes e apague essa linha da planilha do Google depois.
- Se o app "dormir" (o plano grátis desliga após um tempo sem uso), basta abrir o link e
  esperar alguns segundos.

## 5. Ver os resultados

Abra o link com `?admin=1` no final (ex.: `https://seu-app.streamlit.app/?admin=1`) e digite a
senha. O painel mostra a nota SUS média, a taxa de sucesso, o tempo médio e os erros por tarefa,
e tem o botão **Baixar planilha preenchida (.xlsx)**, que coloca até 5 sessões na planilha do
kit (abas SUS e Tarefas), trocando os nomes por P1 a P5; o painel mostra qual nome virou
qual código. Tarefas marcadas como **Revisar** ficam em branco, com um comentário,
para você decidir lendo a resposta e o comentário do participante na planilha do Google.
A aba **Problemas** da planilha do kit continua sendo preenchida por você, a partir dos
comentários.

## Limitações a citar no artigo

- O teste é **remoto e sem moderação**: não há observação direta nem protocolo de pensar em voz
  alta. Os comentários escritos depois de cada tarefa substituem, em parte, essa observação.
- O "erro" registrado é a tentativa de registrar que terminou com mensagem de erro. Erros que
  não geram mensagem (como tocar no botão errado) só aparecem se o participante os comentar.
- O resultado automático segue o gabarito do kit; os casos "Revisar" dependem da sua leitura.
