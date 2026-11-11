# Paridade funcional e limites

| IEC104 CSV Studio | Engineering Copilot Studio | Verificação |
| --- | --- | --- |
| Dashboard: análise e auditoria | IEC 104 → Análise | Golden Master/Slave |
| Comparação entre CSVs | IEC 104 → Análise → Comparar | Comparação canônica |
| Master → Slave | IEC 104 → Conversão | Plano, SHA-256 e exportação |
| Slave → Master | IEC 104 → Conversão | Estratégia de comando, plano e exportação |
| Lista de aquisição | IEC 104 → Listas de pontos | XLSX a partir do Golden Master |
| Lista de distribuição | IEC 104 → Listas de pontos | XLSX a partir do Golden Slave |
| Perfis de regra | IEC 104 → Perfis | CRUD via ProfileStore |
| Golden Files | IEC 104 → Dados de referência | Atribuição por papel e inclusão de CSV |
| Colunas padrão e ObjectTypes | IEC 104 → Dados de referência; Análise → tipos_objeto | Configuração e catálogo descoberto |

Os serviços de domínio e conversão originais foram mantidos. A nova interface usa esses serviços diretamente; não reproduz a interface QML original. O plano de conversão deve ser gerado antes da exportação e o SHA-256 da origem é revalidado.

## Gateway API

O desenho offline cobre identificação de fonte, caminho JSON, valor, escala, unidade, qualidade, timestamp, CA, IOA e ASDU. Não existe conexão de rede ou servidor IEC 104 nesta versão. A configuração exportada tem mode: offline_model.

## Elipse E3

A análise lê o contêiner OLE/EFS, enumera objetos e propriedades selecionadas e registra hash e cobertura. Sem as bibliotecas e o runtime E3, vínculos indiretos, scripts e comandos não podem ser declarados conformes. A UI mostra as primeiras 1.000 linhas; a exportação JSON contém todas.
