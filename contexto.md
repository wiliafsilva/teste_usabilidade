# Contexto do projeto (para retomar o trabalho)

> Atualizado em 09/11/2026. Resumo rápido para quem pega o projeto no meio (inclusive uma nova sessão com IA).
> O histórico completo e a lista de tarefas estão em [diario.md](diario.md).

## 1. Quem, o quê e quando

- **Disciplina:** Laboratório de Engenharia de Software, UNIT, Prof. Sérgio Santana, Ciência da Computação.
- **Aluna:** Wilia Francisco da Silva (equipe de 1 pessoa, autorizada), wilia.francisco@souunit.com.br.
- **Projeto:** Caso 15 · Reserva de laboratórios da faculdade.
  - Regra principal: reservas de 1 a 4 horas, até 40 alunos (o Lab 202 tem 30 lugares).
- **Artigo:** Tema 6 · Teste de usabilidade em aplicativos. É um estudo de caso, com teste feito por 5 colegas.
  - Título: "Teste de Usabilidade com Cinco Usuários: Estudo de Caso de um Sistema de Reserva de Laboratórios".
- **Entrega final, 30/11/2026:** artigo em PDF, planilha de testes, lista de defeitos e apresentação.
- **Prazo do teste com os colegas:** até 22/11/2026.

## 2. Regras de trabalho (não quebrar)

1. Seguir **à risca** as etapas do PDF do professor (`Artigo/projeto/Projeto_Engenharia_de_Software_com_sistemas (2).pdf`), aula por aula, sem pular nenhuma.
2. Cada entrega vai em `Artigo/entrega/entrega-DD-MM-26/`, em `.tex`, `.pdf` e `.docx`, com o título da aula no nome do arquivo.
3. O checklist "Antes de entregar, confira" do PDF **serve só para conferir**; ele não entra nos documentos.
4. **Discutir antes de fazer** quando a decisão for da aluna.
5. **Defeitos do sistema:** a aluna testa primeiro. A IA só confere ou revela defeitos quando ela pedir.
6. **Nunca** apresentar dados simulados ou gerados por IA como se fossem de participantes reais. As sessões simuladas já foram apagadas.
7. **Nunca** colar a chave da conta de serviço do Google no chat nem enviá-la ao GitHub. `chave/`, `*.json` e `.streamlit/secrets.toml` estão no `.gitignore`.
8. Atualizar o `diario.md` ao fim de cada etapa.
9. **Artigo:**
   - modelo SBC, espaçamento 1,5, citações autor-data (ABNT), de 8 a 10 páginas;
   - 5 referências ou mais, sendo 2 ou mais artigos científicos;
   - toda fonte citada (texto copiado sem citação zera o artigo);
   - a Declaração de Uso de IA é obrigatória.

## 3. Onde está cada coisa

| Caminho | O que é |
|---|---|
| `diario.md` | Diário: o que foi feito, o que falta e o registro das sessões |
| `Artigo/projeto/` | Enunciado do professor (PDF) |
| `Artigo/laboratório/` | Sistema avaliado, v1.0: um único HTML |
| `Artigo/templates/` | Modelo SBC (.tex e .docx) |
| `Artigo/entrega/entrega-26-10-26/` | Aula 1 ✅ Requisitos, escopo e histórias |
| `Artigo/entrega/entrega-09-11-26/` | Aula 2 ✅ Tarefas, Kanban, cronograma, riscos e fontes |
| `Artigo/entrega/entrega-16-11-26/` | Aula 3 ✅ 3 camadas, 3 telas e introdução |
| `Artigo/entrega/entrega-23-11-26/` | Aula 4 ✅ App × site, dados e fundamentação |
| `Artigo/Artigo_entrega/artigo-teste-usabilidade.tex` | Artigo: introdução e fundamentação prontas; 9 marcas `\pendente{}` |
| `Artigo/teste-usabilidade/` | Kit do teste (roteiro, tarefas T1 a T5 com gabarito, SUS) e a planilha `.xlsx` que calcula tudo; a pasta `colegas/` (vazia) é para os dados reais |
| `app-teste-usabilidade/` | App Streamlit do teste remoto (detalhes na seção 5) |
| `ferramentas/compilar.sh` | `bash ferramentas/compilar.sh {1\|2\|3\|4\|artigo\|kit}`: gera o PDF e os PNGs das figuras |
| `ferramentas/docx_*.py`, `planilha_teste.py` | Geram os `.docx` e a planilha do kit |
| `ferramentas/copiar_para_artigo.py` | Copia a parte do artigo de uma entrega para o arquivo do artigo |

## 4. Situação atual

- **Aulas 1 a 4:** prontas.
- **Artigo:** introdução e fundamentação prontas. Faltam:
  - 3.1 a 3.4 do Desenvolvimento;
  - as Considerações;
  - o resumo e o abstract;
  - a Declaração de IA.
- **Referências:** F1 a F5 conferidas, com DOIs em F1, F2 e F4.
  - F1 Nielsen & Landauer 1993
  - F2 Nielsen & Molich 1990
  - F3 Brooke 1996
  - F4 Bangor, Kortum & Miller 2008
  - F5 Barbosa & Silva 2010
- **Defeitos encontrados (4 de 15, a meta do professor):**
  - D01, RN07: aceita horários que se cruzam.
  - D02, RN08: cancelar não libera o horário.
  - D03, RN15: a busca ignora a disciplina.
  - D04, RN16: o painel de amanhã soma as reservas canceladas.
- **Teste de usabilidade:** passou a ser **remoto e sem moderação**, pelo app. A planilha do Google e a conta de serviço já estão configuradas e a conexão funciona. **Falta:**
  1. a aluna testar o app no computador e no celular;
  2. ~~publicar no Streamlit Cloud~~ ✅ https://testedeuso.streamlit.app/ (falta deixar o acesso público);
  3. enviar o link aos 5 colegas;
  4. aplicar o teste até 22/11.

## 5. App do teste (`app-teste-usabilidade/`)

- **Rodar localmente:** `streamlit run app.py`. O painel da pesquisadora fica em `?admin=1` e pede senha.
- **Fluxo do participante:**
  1. Início: nome, aparelho, se já reservou, termo de consentimento.
  2. Instruções.
  3. 5 tarefas com o sistema embutido. O texto da tarefa fica num cartão preso no topo; nas tarefas 2 e 5 o campo de resposta também fica no cartão.
  4. Opinião depois de cada tarefa:
     - 11 dificuldades prontas para marcar;
     - um comentário opcional;
     - "Não tive dificuldade" não pode ser marcado junto com outra opção.
  5. Questionário SUS.
  6. Fim, com download de reserva caso a gravação falhe.
- **Avaliação automática:** cada tarefa recebe Sucesso, Falha ou Revisar, comparada com o gabarito do kit. Os casos "Revisar" a aluna decide à mão.
- **Dados:** gravados na aba `Sessoes` da planilha do Google "Teste de usabilidade · respostas", com **49 colunas**. O app reescreve o cabeçalho sozinho se ele mudar; linhas antigas de teste devem ser apagadas.
- **Painel:**
  - métricas e tabela por tarefa;
  - contagem das dificuldades;
  - exporta para a planilha do kit trocando os nomes por códigos P1 a P5 (o nome não sai do Google Sheets).
- **Arquivos:**
  - `app.py`;
  - `gerar_componente.py`: injeta o HTML do sistema em `componente_sistema/`;
  - `gerar_secrets.py`;
  - `modelo_planilha.xlsx`;
  - `README.md`: passo a passo do deploy.
- **Testes:** 85 verificações automáticas passaram (script de teste fora do projeto, na pasta temporária da sessão).

## 6. Próximos passos, em ordem

1. Testar o app (computador e celular). Publicar no Streamlit Cloud: repositório no GitHub e o conteúdo do `secrets.toml` colado em *Secrets*.
2. Enviar o link aos 5 colegas e aplicar o teste **até 22/11**.
3. Exportar pelo painel, decidir os casos "Revisar" e calcular:
   - a taxa de sucesso;
   - o tempo médio;
   - o SUS de cada participante e a média.
4. Classificar cada problema por heurística de Nielsen e por impacto: **alto** se impediu, **médio** se atrasou ou exigiu nova tentativa, **baixo** se foi só dúvida ou incômodo. Propor uma melhoria para cada um.
5. **Aula 5 (até 28/11):**
   - 10 casos de teste, cada um citando uma RN;
   - valores limite: duração 0, 1, 4 e 5 h; alunos 40 e 41 (Lab 202: 30 e 31);
   - Desenvolvimento do artigo escrito com os **dados reais**.
6. **Aula 6 (30/11):**
   - executar os casos de teste;
   - registrar defeitos (meta 15) e propor correções;
   - apresentação de 5 min.
7. **Fechar o artigo:**
   - Considerações, com as limitações abaixo;
   - resumo e abstract;
   - Declaração de IA;
   - figuras;
   - conferir o tamanho (8 a 10 páginas);
   - tirar todas as marcas `\pendente{}`.

## 7. Limitações a citar no artigo

- O teste foi remoto e sem moderação: houve comentários escritos em vez de pensar em voz alta.
- As respostas prontas de dificuldade podem induzir o participante a marcar algo.
- Os colegas fizeram o papel de professores.
- A amostra é pequena (5 participantes), o que está de acordo com Nielsen & Landauer (1993).

---

## 8. Histórico da conversa, em ordem

1. **Leitura do material.** Lemos as pastas: o PDF do projeto, o Laboratório de Sistemas com os 15 casos e os modelos SBC. A aluna escolheu o **Tema 6** e pediu para discutir antes de fazer qualquer coisa.
2. **Escolha do caso.** Comparamos os 15 casos (que também estão no Laboratório de Sistemas) para ver qual combina com teste de usabilidade. Foi escolhido o **Caso 15**, reserva de laboratórios.
3. **Seguir as etapas à risca.** A aluna pediu para seguir o PDF de forma absoluta, aula por aula.
4. **Aula 1.** Gerada em `.tex`, `.pdf` e `.docx`. Os ajustes pedidos foram:
   - nome da disciplina no lugar de "assunto" no cabeçalho;
   - equipe só com Wilia;
   - histórias com alunos? Decisão: alunos **fora do escopo**; as histórias são de professor e coordenação;
   - nomes das pastas no formato `entrega-26-10-26`.
5. **Adiantar as entregas.** Decidimos adiantar todas as aulas para escrever o artigo depois de tudo aprovado.
6. **Regra da IA.** A aluna avisou que a regra "a IA só revisa o português" foi retirada. O PDF novo, `(2)`, confirmou isso; o resto ficou igual. O trabalho pode ser feito sozinho.
7. **Aula 3** criada (camadas e 3 telas), mais a introdução do artigo.
8. **Sobreposição de horários.** A aluna mostrou um print com dois horários se cruzando: é o **D01**. Ficou claro que identificar defeitos é tarefa da **aula 6**; a 5 escreve os casos de teste. Combinado: a aluna testa primeiro.
9. **Artigo.** Começou no modelo SBC do professor, com o e-mail da aluna.
10. **Revisão da aula 1.** Primeiro a aluna testou; depois, a pedido dela, a IA testou com um script e achou **D02, D03 e D04**.
    - RF02 a RF05 viraram "Atende parcialmente", com notas de rodapé citando as RNs.
    - A aluna mostrou a lista de RNs da tela do sistema (18 regras) e a instrução do professor para a aula 1.
    - Combinado: 10 requisitos funcionais **ou mais**. Foi criada a coluna "Regras", ligando as 18 RNs aos requisitos.
11. **Efeitos nas outras aulas.** Conferimos se as mudanças da aula 1 afetavam as demais. O checklist ("item 6" do PDF) saiu dos documentos, porque é só para controle.
12. **`diario.md` criado**, com o curso (Ciência da Computação) e a disciplina (Laboratório de Engenharia de Software).
13. **Ajustes nas aulas 1 e 2:**
    - tarefa **T14** criada na aula 2 (corrigir RF02 a RF05), e o Kanban ficou só com o RF01 em "Feito";
    - RF03 ampliado para "cancelar ou excluir" e RF04 para "listar e buscar".
14. **Referências.** As 5 foram conferidas online (ACM, DBLP, Taylor & Francis, SBC) e os DOIs entraram no artigo e nas aulas 2 e 3.
15. **Aula 4** feita: app × site, diagrama dos dados e fundamentação. Ao conferir Barbosa & Silva (2010) online, a lista de fatores e a escala de gravidade de 0 a 4 **não foram confirmadas** nessa edição. A aluna escolheu "Deixar seguro agora": os dois trechos saíram e os problemas passaram a ser classificados por **impacto** (alto, médio ou baixo). Também foi retirada uma menção solta a "gravidade".
16. **Kit do teste**, para celular: roteiro, termo, cartões, ficha, SUS e planilha com fórmulas (46 conferências).
17. **Fichas e planilha que vieram marcadas como sessões simuladas por IA.**
    - A aluna enviou fichas e uma planilha preenchidas que traziam a marca "Sessão simulada… interpretada por IA".
    - Depois enviou de novo sem a marca, dizendo que eram reais e que só tinha esquecido de tirar a simulação.
    - A IA **não aceitou** usá-las como dados de colegas.
    - A pedido da aluna, os arquivos foram **apagados**, e o teste será refeito com pessoas reais.
18. **Teste remoto.** A aluna pediu um sistema online em **Streamlit** para o teste. Escolhas: remoto, sem moderação, gravando no **Google Sheets**. O app foi criado.
19. **Ajustes no app pedidos pela aluna:**
    - o participante digita o **nome** em vez de um código;
    - a pergunta "onde salvo a planilha?": no Google Sheets, com exportação pelo painel;
    - **configuração da conta Google**, passo a passo: projeto `teste-de-usabilidade-514218` no Google Cloud, API do Sheets e do Drive, conta de serviço, chave JSON em `chave/`, `gerar_secrets.py` e a planilha compartilhada com a conta de serviço;
    - o app rodou localmente (Network URL `http://192.168.15.10:8501`).
20. **Defeito no app relatado pela aluna:** não dava para voltar e rever os dados da tarefa.
    - Solução: um **cartão fixo no topo** com o texto da tarefa.
    - O campo de resposta das tarefas 2 e 5 foi para dentro do cartão.
    - Ganharam botão "Voltar" as instruções e a tela de opinião, que também repete a tarefa.
21. **Respostas prontas na opinião.** Foram criadas 11 opções de dificuldade para marcar. O comentário ficou opcional, foi criada a coluna `tN_dificuldades` e o painel ganhou a contagem. O cabeçalho passou de 44 para 49 colunas.
22. **Este arquivo `contexto.md`** foi criado.

## 9. Detalhes de cada entrega

### Aula 1 · Entender o problema e definir o escopo
- **Requisitos funcionais:**
  - RF01 **Atende**.
  - RF02 a RF05 **Atende parcialmente**, com notas de rodapé:
    - RF02: RN07 / D01;
    - RF03 (cancelar ou excluir): RN08 / D02;
    - RF04 (listar e buscar): RN15 / D03;
    - RF05: RN16 / D04.
  - RF06 a RF10 **Falta**.
- **Coluna "Regras":**
  - RF01: RN01 a RN06 e RN09 a RN13;
  - RF03: RN08 e RN18;
  - RF04: RN14, RN15 e RN17;
  - RF05: RN16.
- **Requisitos não funcionais:** 3, de usabilidade, desempenho e segurança.
- **Fora do escopo:** 5 itens, entre eles o acesso de alunos.
- **Histórias de usuário:** H01 a H06, cada uma com a coluna "Requisito".

### Aula 2 · Planejar o trabalho
- 14 tarefas (T01 a T14).
- Kanban: só o RF01 em "Feito".
- Cronograma de 4 semanas, 5 riscos e 5 fontes com DOI.

### Aula 3 · Desenhar as partes do sistema
- Figuras em `figuras/`:
  - `camadas`: celular/computador → servidor → banco de dados;
  - `tela1-agenda`, `tela2-nova-reserva` e `tela3-minhas-reservas`, em TikZ convertido para PNG.
- Introdução do artigo.

### Aula 4 · Escolher a solução e organizar os dados
- **App × site, com 5 critérios:**
  - custo: Google Play US$ 25 uma vez; Apple US$ 99 por ano;
  - facilidade;
  - manutenção;
  - uso pela coordenação;
  - avisos.
  - Escolhido: **site responsivo**.
- **Diagrama dos dados:**
  - grupos: Usuário (novo), Reserva, Laboratório e Aviso (novo);
  - ligações: Usuário *faz* Reserva (1:N), Reserva *usa* Laboratório (N:1), Reserva *gera* Aviso (1:N).
- Tabela de cada informação: v1.0 → v2.0.
- Fundamentação:
  - usabilidade e a ISO 9241-11, via Barbosa & Silva;
  - teste com usuários, com a fórmula 1−(1−λ)^i, em que λ≈31% e 5 usuários ≈ 85%;
  - SUS com as faixas de Bangor;
  - heurísticas de Nielsen;
  - síntese.

### Kit do teste: tarefas e gabarito
| Tarefa | Pedido | Sucesso |
|---|---|---|
| T1 | Reservar o Lab 201 na quinta 12/11, 10h–12h, 30 alunos (Profa. Ana Souza, Estrutura de Dados) | Reserva nova com esses dados |
| T2 | Achar a 1ª reserva do Lab 101 | Resposta com terça, 8h–12h e Prof. Danilo |
| T3 | Reservar no sábado 10h–13h para 35 alunos | O sábado vai só até 12h (RN13) e o Lab 202 tem 30 lugares (RN06). Sucesso: sábado 9h–12h no Lab 101, ou explicar. "Revisar" se escolheu outro dia |
| T4 | Cancelar a reserva da T1 | Status "Cancelada" (excluir conta como falha) |
| T5 | Achar pela busca a aula de Banco de Dados | Lab 101, quinta, 19h–22h |

- Limite de 5 minutos por tarefa. Desistir conta como falha.

### Planilha do kit
- Abas: Como usar, Resumo, Listas (oculta), SUS, Tarefas e Problemas.
- SUS: itens ímpares −1, 5 − itens pares, soma × 2,5.
- Faixas de Bangor: abaixo de 50 Inaceitável; de 50 a 70 Marginal; acima de 70 Aceitável.

## 10. Detalhes técnicos

### LaTeX e Word
- pdflatex do MiKTeX (instalado pelo scoop).
- Tabelas que quebram de página usam `xltabular`, com `\endhead`.
- Figuras em TikZ: a versão standalone vira PNG com `pdftoppm`.
- Os `.docx` são gerados com python-docx pela classe `Entrega` (`ferramentas/docx_base.py`). As referências ficam em `REFS`.
- `compilar.sh` compila numa pasta temporária. No kit, ele só cria a planilha se ela ainda não existir.

### Sistema avaliado (HTML v1.0)
- Rota `#caso-15`.
- Dados no `localStorage`, chave `labsis:v2:caso-15`.
- Erros do formulário no elemento `#errs`.
- Reservas iniciais têm id `s0`, `s1`…; as novas têm id `r<timestamp>`.

### App Streamlit
- **`gerar_componente.py`** copia o HTML para `componente_sistema/index.html` e injeta:
  - CSS que esconde o botão `.back`;
  - `#caso-15` forçado;
  - aviso ao app (via `postMessage`) a cada gravação no `localStorage`, com `{reservas, erros, hoje, t}`;
  - limpeza dos dados quando muda a sessão;
  - contagem de erros quando `#errs` aparece.
- **Componente:** `components.declare_component(path=...)`, com o protocolo `streamlit:componentReady` / `setFrameHeight` / `setComponentValue`.
- **Estado:** máquina de etapas em `session_state` (inicio → instrucoes → tarefa → pos → sus → fim).
- **Cartão fixo:** `st.container(key="cartao")` com CSS `position: sticky`. O tema é claro fixo (`.streamlit/config.toml`).
- **Cabeçalho da planilha (49 colunas):**
  - `data_hora, nome, aparelho, ja_reservou, sessao`;
  - por tarefa: `tN_resultado, tN_tempo_s, tN_erros, tN_resposta, tN_dificuldades, tN_comentario`;
  - `sus_q1..q10, sus_nota, mais_facil, mais_atrapalhou, reservas_final`.
- **As 11 dificuldades:**
  1. Não tive dificuldade
  2. Não sabia por onde começar
  3. Não entendi o que algum campo pedia
  4. A mensagem de erro não me ajudou a corrigir
  5. Não encontrei a informação que eu procurava
  6. A busca não encontrou o que eu digitei
  7. Tive que arrastar a tabela para o lado para ver tudo
  8. Fiquei em dúvida se a minha ação tinha funcionado
  9. Tive medo de tocar no botão errado
  10. O sistema aceitou algo que eu achava que não devia
  11. Achei a tela confusa ou com informação demais
- **Google:**
  - gspread 6, com conta de serviço `app-teste@teste-de-usabilidade-514218.iam.gserviceaccount.com`;
  - a chave fica em `chave/` e o `secrets.toml` já foi criado e validado (nunca expor nenhum dos dois).
- **Testes:** feitos com `AppTest`. Depois de `st.rerun()` os widgets ficam desatualizados, então cada etapa é testada separadamente, com o estado já preenchido.

## 11. Problemas que já aconteceram e como foram resolvidos

- **`\usepackage` corrompido.** Um `sed` com `\u` estragou o comando. Foi corrigido à mão, e a troca de `tabularx` para `xltabular` foi feita por script.
- **Geradores de `.docx` perdidos.** Eles ficavam na pasta temporária, que foi apagada. Foram recriados em `ferramentas/`.
- **Problemas de diagramação, todos corrigidos:**
  - tabelas saindo da página;
  - esboços de tela sobrepostos;
  - linha sobrando numa tabela;
  - "Atende par-cialmente" hifenizado;
  - rótulos do diagrama sobrepostos.
- **Citações não confirmadas de Barbosa & Silva.** Foram retiradas do texto.
- **Fichas e planilha marcadas como sessões simuladas por IA.** Foram descartadas e apagadas.
- **App sem como rever a tarefa.** Foi criado o cartão fixo.

## 12. Regras ainda não testadas (aula 6)
- RN01 a RN06, RN09 a RN14, RN17 e RN18. A aluna testa primeiro; a IA só confere quando ela pedir.
