# Diário do projeto: Engenharia de Software + Artigo

> Última atualização: 09/11/2026

## 1. Visão geral

| Item | Definição |
|---|---|
| Disciplina | Laboratório de Engenharia de Software |
| Professor | Sérgio Santana |
| Integrante | Wilia Francisco da Silva (equipe de 1 pessoa; o professor autorizou) |
| E-mail | wilia.francisco@souunit.com.br |
| Curso | Ciência da Computação (UNIT) |
| Caso do projeto | **15 · Reserva de laboratórios da faculdade** |
| Regra para testar | Reservas de 1 a 4 horas, para até 40 alunos (30 no Lab 202) |
| Tema do artigo | **6 · Teste de usabilidade em aplicativos** (estudo de caso, teste com 5 colegas) |
| Pergunta guia | Como testar se um aplicativo é fácil de usar? |
| Entrega final | **30/11/2026**: artigo em PDF, planilha de testes, lista de defeitos e apresentação |

### Regras que valem para tudo
- **Seguir à risca o PDF** do projeto (`Artigo/projeto/Projeto_Engenharia_de_Software_com_sistemas (2).pdf`), aula por aula.
- O checklist "Antes de entregar, confira" **serve só para conferir**; ele não entra nos documentos.
- Cada entrega vai para `Artigo/entrega/entrega-DD-MM-26/`, em `.tex`, `.pdf` e `.docx`, com o nome da aula no arquivo.
- **Defeitos do sistema:** primeiro eu testo; o Claude só confere ou revela quando eu pedir.
- **Artigo:** texto copiado sem citação zera o artigo, então toda fonte precisa ser citada. A regra antiga sobre IA foi retirada pelo professor, mas a Declaração de Uso de IA do modelo SBC continua obrigatória.

### Avaliação
| Projeto | Pontos | Artigo | Pontos |
|---|---|---|---|
| Testes executados e defeitos registrados (aula 6) | 2,0 | Tema e pergunta tratados com clareza | 1,0 |
| Trabalho em equipe | 1,0 | Fundamentação com fontes confiáveis | 2,0 |
| Participação de todos os integrantes | 2,0 | Desenvolvimento com exemplos ou dados próprios | 1,0 |
| | | Escrita, formatação e referências | 1,0 |
| **Total** | **5,0** | **Total** | **5,0** |

---

## 2. Organização das pastas

```
Teste_usabilidade/
├── diario.md                       ← este arquivo
├── app-teste-usabilidade/          ← app Streamlit do teste remoto (ver README.md)
├── ferramentas/                    ← scripts para gerar os PDFs e os Words
│   ├── compilar.sh                 ← bash ferramentas/compilar.sh {1|2|3|4|artigo|kit}
│   ├── copiar_para_artigo.py       ← copia a parte do artigo de uma entrega para o artigo
│   └── docx_base.py, docx_aula1.py ... docx_aula4.py
└── Artigo/
    ├── projeto/                    ← PDF do professor (enunciado)
    ├── laboratório/                ← sistema v1.0 (laboratorio-de-sistemas (3).html)
    ├── templates/                  ← modelo SBC (.tex e .docx) e exemplo preenchido
    ├── entrega/
    │   ├── entrega-26-10-26/       ← Aula 1
    │   ├── entrega-09-11-26/       ← Aula 2
    │   ├── entrega-16-11-26/       ← Aula 3 (+ figuras/)
    │   ├── entrega-23-11-26/       ← Aula 4 (+ figuras/)
    │   ├── entrega-DD-11-26/       ← Aula 5 (data a combinar, até 28/11)
    │   └── entrega-30-11-26/       ← Aula 6 (a fazer)
    ├── teste-usabilidade/          ← kit do teste (referência) + planilha .xlsx + colegas/ (dados reais)
    └── Artigo_entrega/
        └── artigo-teste-usabilidade.tex / .pdf   ← artigo (modelo SBC)
```

---

## 3. Cronograma geral

| Aula | Data | Projeto (Caso 15) | Artigo (Tema 6) | Situação |
|---|---|---|---|---|
| 1 | 26/10 | Requisitos, qualidades, escopo e histórias | Escolher o tema | ✅ Pronta |
| 2 | 09/11 | Tarefas, Kanban, cronograma e riscos | 5 fontes | ✅ Pronta |
| 3 | 16/11 | 3 camadas e 3 telas | Introdução | ✅ Pronta |
| 4 | 23/11 | Comparar app × site e organizar os dados | Fundamentação teórica | ✅ Pronta |
| 5 | até 28/11 | 10 casos de teste com valores limite | Desenvolvimento/análise (entrega até 22h) | ⬜ A fazer |
| 6 | 30/11 | Executar os testes, registrar defeitos e apresentar | Artigo final em PDF | ⬜ A fazer |
| — | **até 22/11** | — | **Aplicar o teste de usabilidade com 5 colegas** | ⬜ A fazer |

---

## 4. O que já foi feito

### Aula 1 · 26/10 · Entender o problema e definir o escopo ✅
Pasta: `Artigo/entrega/entrega-26-10-26/`
- [x] O problema (contexto do Caso 15)
- [x] 10 requisitos funcionais (RF01 a RF10), cada um classificado na v1.0:
  - RF01 Atende
  - RF02 a RF05 Atende parcialmente, com notas que citam as RNs
  - RF06 a RF10 Falta
- [x] Coluna "Regras": as 18 RNs da tela estão ligadas aos requisitos (RF03 ampliado para "cancelar ou excluir" e RF04 para "listar e buscar")
- [x] 3 requisitos não funcionais: usabilidade, desempenho e segurança
- [x] O que fica fora do sistema (5 itens, incluindo o acesso de alunos)
- [x] 6 histórias de usuário, cada uma ligada a um requisito
- [x] Tema do artigo escolhido

### Aula 2 · 09/11 · Planejar o trabalho ✅
Pasta: `Artigo/entrega/entrega-09-11-26/`
- [x] 14 tarefas da v2.0 (T01 a T14), com origem, semana e responsável; a T14 corrige RF02 a RF05 (D01 a D04)
- [x] Quadro Kanban (A fazer, Fazendo e Feito); só o RF01 fica em "Feito"
- [x] Cronograma de 4 semanas (a T14 está na semana 1)
- [x] 5 riscos com ação (inclui o risco de alterar um sistema em uso)
- [x] 5 fontes do artigo (3 artigos científicos)

### Aula 3 · 16/11 · Desenhar as partes do sistema ✅
Pasta: `Artigo/entrega/entrega-16-11-26/`
- [x] Diagrama em 3 camadas (celular/computador, servidor e banco de dados), tabela do que fica em cada camada e o caminho de uma reserva
- [x] Esboço das 3 telas da v2.0: Agenda, Nova reserva e Minhas reservas, ligadas às histórias
- [x] Introdução do artigo
- [ ] *Opcional:* desenhar as telas à mão, se o professor exigir "no papel"

### Aula 4 · 23/11 · Escolher a solução e organizar os dados ✅
Pasta: `Artigo/entrega/entrega-23-11-26/`
- [x] Tabela **aplicativo instalado × site que abre no celular** com 5 critérios: custo, facilidade para o usuário, manutenção, uso pela coordenação e avisos (taxas das lojas conferidas: Google US$ 25 uma vez; Apple US$ 99/ano)
- [x] Escolha: **site que abre no celular**, justificada pelo problema do caso (agenda única e ao mesmo tempo para todos), pelo RNF01 e pelos riscos R01 e R04
- [x] Diagrama dos dados com 4 grupos ligados por setas: Usuário (novo), Reserva, Laboratório e Aviso (novo), com "+" no que entra na v2.0
- [x] Tabela de cada informação: onde aparece na v1.0 e o que muda na v2.0
- [x] **Artigo:** fundamentação teórica (usabilidade, teste com usuários e os 5 participantes, SUS com as faixas de Bangor, heurísticas e síntese)

### Artigo ✅ (em andamento)
Pasta: `Artigo/Artigo_entrega/`
- [x] Montado sobre o modelo SBC do professor, com espaçamento 1,5 e citações autor-data (ABNT)
- [x] Título em português e inglês, autor e e-mail
- [x] Introdução completa
- [x] Fundamentação teórica completa (copiada da aula 4 com `ferramentas/copiar_para_artigo.py`)
- [ ] Seções 3 (Desenvolvimento) e 4 (Considerações), resumo, abstract e declaração de IA ainda marcados como [PENDENTE]
- [x] 5 referências
- [x] Curso preenchido no cabeçalho (Ciência da Computação)

### Fontes do artigo
| Nº | Referência | Tipo | Uso |
|---|---|---|---|
| F1 | Nielsen & Landauer (1993), INTERCHI'93 | Artigo científico | Por que 5 usuários |
| F2 | Nielsen & Molich (1990), CHI'90 | Artigo científico | Heurísticas |
| F3 | Brooke (1996), SUS | Capítulo de livro | Questionário SUS |
| F4 | Bangor, Kortum & Miller (2008), IJHCI | Artigo científico | Interpretar a nota do SUS |
| F5 | Barbosa & Silva (2010), Elsevier | Livro | Conceito de usabilidade |

- [x] **5 referências conferidas em 09/11/2026**: autores, ano, local, volume e páginas batem com as fontes
  - DOIs: F1 10.1145/169059.169166 · F2 10.1145/97243.97281 · F4 10.1080/10447310802205776
  - [x] DOIs acrescentados às referências do artigo, da aula 2 (tabela de fontes) e da aula 3 (referências da introdução)
  - F3: editores JORDAN, P. W.; THOMAS, B.; WEERDMEESTER, B. A.; McCLELLAND, I. L.
  - F5: ISBN 978-85-352-3418-3 (Elsevier, 2010); existe uma edição nova de 2021 ("IHC e Experiência do Usuário"), mas citamos a de 2010

---

## 5. Defeitos encontrados no sistema (para a aula 6)

Meta do professor: **15 defeitos**. Encontrados: **4**.

| Nº | Regra | Defeito | Passos | Esperado | Obtido | Correção proposta | Quem achou |
|---|---|---|---|---|---|---|---|
| D01 | RN07 | Aceita reservas com horários que se cruzam | Reservar Lab 101 em 06/11 das 19h às 22h; depois, das 20h às 21h | Recusar a 2ª | As duas são aceitas | Recusar quando início_nova < fim_existente e fim_nova > início_existente (ignorando canceladas) | Wilia |
| D02 | RN08 | Cancelar não libera o horário | Cancelar uma reserva e reservar o mesmo lab, data e horário | Aceitar | Recusa: "já está reservado nesse horário" | Ignorar reservas canceladas na verificação de choque | Claude (teste a pedido) |
| D03 | RN15 | A busca não encontra pela disciplina | Buscar "Redes" ou "Banco de Dados" | Achar as reservas | 0 resultados | Incluir a disciplina nos campos da busca | Claude (teste a pedido) |
| D04 | RN16 | O painel de amanhã soma as canceladas | Ver "Ocupação de amanhã" com uma reserva cancelada amanhã | Lab 201: 0 h | Lab 201: 2 h | Filtrar as canceladas antes de somar | Claude (teste a pedido) |

Regras ainda não testadas: RN01 a RN06, RN09 a RN14, RN17 e RN18.

---

## 6. O que falta fazer

### Decisões e ajustes pendentes
- Nenhum no momento.

### Teste de usabilidade com 5 colegas (base do artigo) · até 22/11
- [x] **Kit pronto** em `Artigo/teste-usabilidade/` (09/11): roteiro com gabarito, termo de consentimento, 5 cartões de tarefa, ficha de observação, questionário SUS e planilha que calcula tudo (fórmulas conferidas)
  - Aparelho: **celular**. Tarefas: (1) reservar Lab 201 na quinta 10h–12h; (2) achar a 1ª reserva do Lab 101; (3) reservar no sábado 10h–13h para 35 alunos; (4) cancelar a reserva da tarefa 1; (5) achar pela busca a aula de Banco de Dados
  - Imprimir: roteiro ×1, termo ×5, cartões ×1 jogo, ficha ×5, SUS ×5
- [x] **Mudança de formato (09/11):** o teste passa a ser **remoto, sem moderação**, pelo app `app-teste-usabilidade/` (Streamlit + Google Sheets). Sessões simuladas por IA foram descartadas e apagadas; não entram no artigo.
- [ ] Testar o app no computador (`streamlit run app.py`) e conferir o sistema embutido
- [x] Criar a planilha do Google e a conta de serviço; publicar no Streamlit Cloud (09/11): https://testedeuso.streamlit.app/ (repositório privado `wiliafsilva/teste_usabilidade`)
- [ ] Deixar o app aberto para quem não tem conta (Settings → Sharing → público) e fazer uma sessão de teste no link publicado; depois apagar essa linha da planilha
- [ ] Enviar o link com um código (P1 a P5) para cada colega
- [ ] **Aplicar o teste com os 5 colegas**
- [ ] Exportar pelo painel (`?admin=1`) para a planilha do kit e decidir os casos "Revisar"; organizar os resultados: taxa de sucesso, tempo médio, nota SUS (individual e média) e lista de problemas
- [ ] Classificar cada problema por heurística de Nielsen e por impacto na tarefa (alto: impediu; médio: atrasou ou exigiu nova tentativa; baixo: só dúvida ou incômodo)
- [ ] Propor uma melhoria para cada problema (v2.0)

### Aula 5 · até 28/11 · Escrever casos de teste
Pasta: `Artigo/entrega/entrega-DD-11-26/` (data a combinar)
- [ ] Planilha com **10 casos de teste** a partir das regras de negócio da tela, cada um citando a RN
- [ ] Cada caso tem passos, dados e resultado esperado
- [ ] Há casos que devem dar certo e casos que devem dar erro
- [ ] **Valores limite** da regra do caso: duração 0, 1, 4 e 5 h; alunos 40 e 41 (Lab 202: 30 e 31)
- [ ] **Artigo:** escrever o desenvolvimento/análise (3.1 Sistema avaliado, 3.2 Planejamento do teste, 3.3 Resultados, 3.4 Análise e propostas)
- [ ] Copiar o desenvolvimento para o arquivo do artigo
- [ ] **Entrega até 22h:** planilha + desenvolvimento do artigo

### Aula 6 · 30/11 · Executar os testes e apresentar
Pasta: `Artigo/entrega/entrega-30-11-26/`
- [ ] Executar os 10 casos de teste no sistema e anotar o que passou e o que falhou
- [ ] Registrar cada defeito com a RN, os passos, o resultado esperado e o obtido (meta: 15)
- [ ] Propor a correção de cada defeito
- [ ] Apresentação de 5 minutos com pelo menos um item de cada aula: requisitos, planejamento, desenho do sistema e testes
- [ ] **Entrega até 22h:** planilha com o resultado de cada teste, lista de defeitos, apresentação e artigo final

### Fechamento do artigo · até 30/11
- [ ] Considerações finais: resposta à pergunta, achados, limitações (colegas no papel de professores) e trabalhos futuros
- [ ] Resumo e Abstract (um parágrafo cada) com as palavras-chave
- [ ] Declaração de Uso de IA (ferramenta, etapas e finalidade)
- [ ] Inserir figuras e tabelas (arquitetura, telas, resultados e SUS)
- [ ] Conferir que todas as citações estão nas referências e vice-versa
- [ ] Conferir **de 8 a 10 páginas**, Times 12, espaçamento 1,5, **5 referências ou mais (2 ou mais artigos científicos)**, modelo SBC
- [ ] Remover todas as marcas [PENDENTE]
- [ ] Revisar o português
- [ ] **Gerar o PDF final e entregar em 30/11**

---

## 7. Registro das sessões

### 29/10/2026
- Lemos o material: PDF do projeto, Laboratório de Sistemas e modelos SBC.
- Escolhas: Caso 15 + Tema 6.
- Entregas das aulas 1, 2 e 3 criadas, em .tex, .pdf e .docx.
- O professor enviou um PDF novo: saiu a frase "a IA só pode revisar o português"; o resto ficou igual.
- Esqueleto do artigo criado no modelo SBC, com a introdução.
- Defeitos D01 a D04 encontrados; aula 1 reclassificada (RF02 a RF05 como "Atende parcialmente").
- Histórias da aula 1 ligadas aos requisitos; checklist retirado das entregas.

### 09/11/2026
- Aula 1: RF03 ampliado para "Cancelar ou excluir" e RF04 para "Listar e buscar"; nova coluna "Regras" ligando as 18 RNs aos requisitos.
- Aula 2: nova tarefa T14 (corrigir RF02 a RF05 / D01 a D04) na semana 1; no Kanban, só o RF01 ficou em "Feito"; risco R02 ajustado.
- Os scripts de geração dos .docx foram recriados na pasta `ferramentas/` (a pasta temporária anterior foi apagada).
- Referências F1 a F5 conferidas em bases bibliográficas (ACM, DBLP, Taylor & Francis e SBC): todas corretas.
- DOIs de F1, F2 e F4 acrescentados no artigo e nas aulas 2 e 3 (.tex, .pdf e .docx).
- Para a fundamentação (aula 4): explicar que o "5 usuários ≈ 85%" vem do modelo de Nielsen & Landauer (cada usuário acha em média ~31% dos problemas) e que Nielsen recomendava várias rodadas pequenas de 5.
- Aula 4 feita: comparação app × site (escolhido o site), diagrama dos dados (Usuário, Reserva, Laboratório, Aviso) e fundamentação teórica; a fundamentação também foi para o artigo (5 páginas).
- Ferramentas: `compilar.sh` agora gera os PNGs das figuras e aceita a aula 4; novo `copiar_para_artigo.py`.
- Citações de Barbosa & Silva (2010) verificadas online: a definição da ISO 9241-11 foi confirmada; a lista de fatores e a escala de gravidade de 0 a 4 não foram confirmadas na edição de 2010 (a escala é de Nielsen e aparece citada pela edição de 2021). Decisão: retirar os dois trechos; os problemas passam a ser classificados por heurística e por impacto na tarefa (alto, médio ou baixo).
- Kit do teste de usabilidade criado (aparelho: celular), com PDF, Word e planilha; as 46 conferências das fórmulas da planilha bateram.
- O teste de usabilidade passa a ser remoto: app Streamlit (`app-teste-usabilidade/`) com o sistema embutido, avaliação automática das tarefas, SUS e gravação no Google Sheets; 56 verificações automáticas passaram.
- Para o artigo: descrever o teste como remoto e sem moderação (comentários escritos em vez de pensar em voz alta) e citar isso nas limitações.
- Código enviado ao GitHub (repositório privado; chave e `secrets.toml` não foram junto) e app publicado no Streamlit Cloud: https://testedeuso.streamlit.app/. Para o deploy foi preciso autorizar o Streamlit a ver repositórios privados e usar `/` no caminho do arquivo (`app-teste-usabilidade/app.py`).
