# Engineering Copilot Studio

Aplicação desktop open source em Python para engenharia IEC 104, modelagem de gateways REST/JSON, inspeção estática de projetos Elipse E3 e gestão de skills.

## O que funciona

| Área | Fluxos disponíveis |
| --- | --- |
| IEC 104 | Analisar e auditar CSV E3; comparar dois CSVs; planejar e executar Master → Slave e Slave → Master; gerar listas de aquisição e distribuição em XLSX; criar, editar e remover perfis; administrar Golden Files e colunas padrão. |
| Gateway API | Modelar pontos de uma amostra JSON, validar CA/IOA/ASDU e direção, conferir qualidade e timestamp, pré-visualizar valores e exportar configuração JSON. |
| Elipse E3 | Ler .prj e .lib sem alterar os originais; registrar SHA-256, cobertura de nós, objetos, classes e propriedades selecionadas; comparar versões e exportar relatório JSON. |
| Skills | Consultar os fluxos integrados, importar um SKILL.md ou uma pasta com várias skills e pesquisar o catálogo. |

O gateway funciona **offline** nesta versão. Ele não consulta APIs, não inicia um servidor IEC 104 e não envia comandos. A inspeção E3 não comprova a resolução de vínculos indiretos, bibliotecas externas nem o comportamento em execução; o relatório marca esse escopo como **NÃO INSPECIONADO**.

## Instalação

Requer Python 3.12 ou superior:

    python -m venv .venv
    .\.venv\Scripts\python.exe -m pip install -e .
    .\.venv\Scripts\engineering-copilot-studio.exe

Nesta máquina, abra iniciar.bat para iniciar a interface com o ambiente virtual já preparado. iniciar.ps1 também encontra o Python 3.13 instalado quando as dependências estão disponíveis. A interface salva perfis, Golden Files e skills no diretório de dados do usuário.

## Organização

- src/engineering_copilot_studio/: interface, gateway offline, catálogo de skills e auditoria E3.
- src/iec104_csv_studio/: núcleo de domínio, conversão e persistência do IEC104 CSV Studio.
- config/ e golden_files/: exemplos editáveis no código fonte.
- src/engineering_copilot_studio/seeds/: cópias usadas no pacote instalado.
- tests/: testes de contratos e fluxos principais.
- docs/PARIDADE.md: correspondência com as funções do IEC104 Converter.

## Adicionar uma skill

Crie uma pasta com SKILL.md:

    ---
    name: minha-skill
    description: Descrição curta da capacidade
    group: Engenharia
    ---

    # Minha skill

    Entradas, sequência de análise, critérios de qualidade e saída esperada.

Na tela **Skills**, escolha **Adicionar SKILL.md** ou **Importar pasta de skills**. Skills em Markdown acrescentam conhecimento ao catálogo e não executam Python. Para novas ferramentas executáveis, implemente um módulo testado e integre a ação à interface.

## Desenvolvimento e testes

    .\.venv\Scripts\python.exe -m pip install -e ".[dev]"
    .\.venv\Scripts\python.exe -m pytest -q

O código é distribuído sob licença MIT. Consulte NOTICE.md para a proveniência dos módulos reaproveitados.
