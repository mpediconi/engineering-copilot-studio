# Proveniência

O núcleo em src/iec104_csv_studio/domain, application e infrastructure foi integrado a partir do projeto do usuário **IEC104 CSV Studio**. A interface desta aplicação é nova. Os Golden Files aqui incluídos são exemplos sintéticos.

O leitor src/engineering_copilot_studio/e3/e3reader.py foi integrado a partir do analisador E3 desenvolvido pelo usuário. Ele não inclui bibliotecas, projetos .prj ou dados operacionais de plantas.

O diretório tools/e3_comparator_original preserva o comparador original completo: comparar.py, e3reader.py, e3base.py, patterns e o visualizador Windows Forms. Os logs históricos não foram migrados; a pasta logs é criada vazia para novas execuções.

Dependências de terceiros: PySide6, openpyxl e olefile mantêm suas próprias licenças.
