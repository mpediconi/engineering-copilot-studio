# Configuração da aplicação

- `app.json`: diretórios funcionais e profile padrão.
- `data_setup.json`: Golden Files atribuídos e padrão de colunas de entrada/saída.
- `profiles/`: profiles IEC104 editáveis em JSON.

Na execução a partir do código-fonte, esta pasta é utilizada diretamente. Em uma
instalação empacotada, os arquivos iniciais são copiados para a área de dados local do
usuário antes da primeira alteração.

Os profiles podem ser criados, alterados e removidos pela tela **Profiles**. Alterações
válidas são persistidas nos arquivos JSON e registradas imediatamente no domínio.
