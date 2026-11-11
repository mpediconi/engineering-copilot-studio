"""Extensible skill catalog: built-in workflows plus user SKILL.md files."""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from pathlib import Path

from .bootstrap import user_data_root


@dataclass(frozen=True)
class Skill:
    key: str
    title: str
    group: str
    description: str
    instructions: str
    action: str | None = None
    source: str = "integrada"


BUILTINS = (
    Skill("iec104-analyze", "Analisar CSV IEC 104", "IEC 104",
          "Classifica Master/Slave, inventaria pontos e audita o CSV E3.",
          "Selecione um CSV, escolha o perfil e analise. Revise os diagnósticos antes de converter.",
          "iec104"),
    Skill("iec104-compare", "Comparar CSVs", "IEC 104",
          "Compara os endereços e a estrutura canônica de dois CSVs.",
          "Selecione dois CSVs de referência e compare o resultado por papel, endereço e função.",
          "iec104"),
    Skill("iec104-master-slave", "Converter Master → Slave", "IEC 104",
          "Planeja, audita e exporta uma conversão verificada.",
          "Gere o plano antes da exportação. Bloqueios impedem a gravação.",
          "iec104"),
    Skill("iec104-slave-master", "Converter Slave → Master", "IEC 104",
          "Converte com estratégia explícita para a fase dos comandos.",
          "Escolha a estratégia de comando, gere o plano e revise perdas e avisos.",
          "iec104"),
    Skill("iec104-acquisition", "Lista de aquisição", "IEC 104",
          "Gera planilha XLSX de pontos para aquisição Master.",
          "Use CSV Master e confira a indicação de papel incompatível.",
          "iec104"),
    Skill("iec104-distribution", "Lista de distribuição", "IEC 104",
          "Gera planilha XLSX de pontos para distribuição Slave.",
          "Use CSV Slave e confira a indicação de papel incompatível.",
          "iec104"),
    Skill("iec104-profiles", "Perfis IEC 104", "IEC 104",
          "Cria, edita e remove regras de auditoria validadas.",
          "Copie um perfil existente e ajuste as regras com revisão técnica.",
          "iec104"),
    Skill("iec104-golden", "Golden Files e colunas", "IEC 104",
          "Administra CSVs de referência e colunas padrão de importação/exportação.",
          "Guarde arquivos de referência separados dos projetos originais.",
          "iec104"),
    Skill("gateway-json", "Mapear API → IEC 104", "Gateway API",
          "Valida mapeamento de JSON para CA/IOA/ASDU e simula valores offline.",
          "Insira amostra JSON; valide endereços, direção e caminhos antes de exportar.",
          "gateway"),
    Skill("e3-static", "Inspecionar projeto E3", "Elipse E3",
          "Inventaria objetos e propriedades selecionadas de .prj/.lib com hash e cobertura.",
          "Use análise estática para levantar evidências; confirme vínculos indiretos no E3.",
          "e3"),
    Skill("engineering-iec104-audit", "Auditoria IEC 104", "Engineering Copilot",
          "Revise papel Master/Slave, CA, IOA, ASDU, comandos, setpoints, timers e janelas.",
          "Separe violações objetivas de recomendações; registre evidência e versão do driver. "
          "Não deduza o tipo de ponto pelo nome nem preencha endereços ausentes."),
    Skill("engineering-point-list", "Normalização de pontos", "Engineering Copilot",
          "Organize discretos, analógicos, comandos e setpoints com rastreabilidade.",
          "Preserve origem, nome, descrição, ASDU, CA e IOA. Marque lacunas e conflitos. "
          "Gere lista pronta para planilha sem inventar campos."),
    Skill("engineering-e3-audit", "Cadeia E3 N1 → N3", "Engineering Copilot",
          "Audite vínculos de leitura e comando entre equipamento, gateway e SCADA.",
          "Registre SHA-256, Source/Fonte, PathName, Name, classe e direção. "
          "Classifique como conforme, divergência comprovada, revisão necessária ou não inspecionado. "
          "Não trate ausência de .Value ou prefixo : como erro isolado."),
    Skill("engineering-mapping", "Governança de mapeamento", "Engineering Copilot",
          "Mantenha linhagem de dados entre API, gateway, IEC 104 e destino SCADA.",
          "Registre fonte, transformação, qualidade, timestamp, destino e versão. "
          "Separe valor observado de regra proposta e verifique colisões de endereço."),
    Skill("engineering-gateway", "Arquitetura de gateway", "Engineering Copilot",
          "Projete aquisição REST, normalização, publicação IEC 104 e observabilidade.",
          "Defina fronteiras, persistência, controle de segredos, estados de falha, "
          "timers e testes de interoperabilidade antes de ativar comunicação real."),
)

_SLUG = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_-]{1,63}$")


def _frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    close = text.find("\n---", 4)
    if close < 0:
        return {}, text
    metadata = {}
    for line in text[4:close].splitlines():
        key, separator, value = line.partition(":")
        if separator:
            metadata[key.strip().lower()] = value.strip().strip('"')
    return metadata, text[close + 4:].strip()


def load_user_skills(directory: Path | None = None) -> list[Skill]:
    directory = directory or user_data_root() / "skills"
    directory.mkdir(parents=True, exist_ok=True)
    result = []
    for path in sorted(directory.glob("*/SKILL.md")):
        try:
            metadata, body = _frontmatter(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError):
            continue
        result.append(Skill(
            key=path.parent.name,
            title=metadata.get("name") or path.parent.name,
            group=metadata.get("group") or "Adicionadas",
            description=metadata.get("description") or "",
            instructions=body,
            source="usuário",
        ))
    return result


def all_skills() -> list[Skill]:
    return [*BUILTINS, *load_user_skills()]


def import_skill(path: str | Path) -> Skill:
    source = Path(path)
    if source.is_dir():
        source = source / "SKILL.md"
    if source.name != "SKILL.md" or not source.is_file() or source.is_symlink():
        raise ValueError("Selecione um arquivo SKILL.md válido.")
    content = source.read_text(encoding="utf-8")
    metadata, body = _frontmatter(content)
    key = (metadata.get("name") or source.parent.name).lower().replace(" ", "-")
    if not _SLUG.fullmatch(key):
        raise ValueError("O nome da skill deve usar letras, números, hífen ou sublinhado.")
    if len(content) > 200_000 or not body:
        raise ValueError("A skill está vazia ou excede 200 KB.")
    destination = user_data_root() / "skills" / key
    if destination.exists():
        raise FileExistsError(f"A skill {key} já está instalada.")
    destination.mkdir(parents=True)
    shutil.copy2(source, destination / "SKILL.md")
    return next(item for item in load_user_skills() if item.key == key)


def import_skill_collection(directory: str | Path) -> tuple[list[Skill], list[str]]:
    root = Path(directory)
    if not root.is_dir():
        raise ValueError("Selecione uma pasta que contenha subpastas com SKILL.md.")
    imported: list[Skill] = []
    skipped: list[str] = []
    for path in sorted(root.glob("*/SKILL.md")):
        try:
            imported.append(import_skill(path))
        except (ValueError, FileExistsError, OSError, UnicodeError) as exc:
            skipped.append(f"{path.parent.name}: {exc}")
    return imported, skipped
