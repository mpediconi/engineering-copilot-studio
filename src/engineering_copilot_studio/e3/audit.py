"""Evidence-oriented static audit of E3 container data."""

from __future__ import annotations

import hashlib
from pathlib import Path

from .e3reader import Project


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def audit_project(path: str) -> dict:
    source = Path(path)
    if source.suffix.lower() not in {".prj", ".lib"}:
        raise ValueError("Selecione um projeto .prj ou uma biblioteca .lib.")
    if not source.is_file():
        raise FileNotFoundError(source)
    digest = sha256_file(source)
    project = Project(str(source))
    try:
        project.build(load_objects=True)
        nodes = list(project.walk())
        objects = []
        links = []
        findings = []
        loaded = 0
        for node in nodes:
            if node.has_data and node.loaded:
                loaded += 1
            if node.has_data and not node.tree_ok:
                findings.append({
                    "estado": "REVISÃO NECESSÁRIA",
                    "evidencia": node.path,
                    "mensagem": "Hierarquia de objetos não reconciliada pelo leitor.",
                })
            for obj in node.objects:
                location = f"{node.path}/{obj.get('opath') or obj.get('name') or obj['idx']}"
                props = {name: value for name, _vt, value, _offset in obj["props"]}
                objects.append({
                    "caminho": location,
                    "classe": obj["class"],
                    "nome": obj["name"],
                    "guid": obj["guid"],
                })
                for prop in ("Source", "Fonte", "PathName", "Name", "N1", "N2", "N3", "N4", "B1", "B2", "B3", "B4"):
                    if prop in props:
                        links.append({
                            "objeto": location,
                            "classe": obj["class"],
                            "propriedade": prop,
                            "valor": str(props[prop]),
                        })
        if loaded < sum(n.has_data for n in nodes):
            findings.append({
                "estado": "NÃO INSPECIONADO",
                "evidencia": source.name,
                "mensagem": "Nem todos os nós com dados foram decodificados.",
            })
        if not links:
            findings.append({
                "estado": "NÃO INSPECIONADO",
                "evidencia": source.name,
                "mensagem": "Nenhuma propriedade de vínculo selecionada foi extraída; confira bibliotecas e exportações E3.",
            })
        findings.append({
            "estado": "NÃO INSPECIONADO",
            "evidencia": source.name,
            "mensagem": (
                "A resolução semântica de Source/Fonte, PathName, bibliotecas externas, "
                "comandos indiretos e comportamento em runtime não foi comprovada."
            ),
        })
        return {
            "arquivo": source.name,
            "bytes": source.stat().st_size,
            "sha256": digest,
            "cobertura": {
                "nos": len(nodes),
                "nos_com_dados": sum(n.has_data for n in nodes),
                "nos_decodificados": loaded,
                "objetos": len(objects),
                "propriedades_selecionadas": len(links),
            },
            "objetos": objects,
            "vinculos": links,
            "achados": findings,
            "limites": [
                "Inspeção estática do contêiner E3; não confirma comportamento em runtime.",
                "Bibliotecas externas, scripts dinâmicos e associações indiretas exigem revisão adicional.",
                "N2 operacional e parâmetro N2 são conceitos distintos; nenhuma equivalência é presumida.",
            ],
        }
    finally:
        project.ole.close()


def compare_projects(before_path: str, after_path: str) -> dict:
    """Compare decoded object identities and selected properties between versions."""
    before = audit_project(before_path)
    after = audit_project(after_path)

    def index(report: dict) -> dict[str, dict]:
        result = {}
        for obj in report["objetos"]:
            identity = obj["guid"] or obj["caminho"]
            result[identity] = obj
        return result

    left = index(before)
    right = index(after)
    added = [right[key] for key in right.keys() - left.keys()]
    removed = [left[key] for key in left.keys() - right.keys()]
    moved = [
        {"guid": key, "de": left[key]["caminho"], "para": right[key]["caminho"]}
        for key in left.keys() & right.keys()
        if left[key]["caminho"] != right[key]["caminho"]
    ]

    def properties(report: dict) -> dict[tuple[str, str], str]:
        return {
            (item["objeto"], item["propriedade"]): item["valor"]
            for item in report["vinculos"]
        }

    left_props, right_props = properties(before), properties(after)
    changed = [
        {
            "objeto": key[0],
            "propriedade": key[1],
            "de": left_props[key],
            "para": right_props[key],
        }
        for key in left_props.keys() & right_props.keys()
        if left_props[key] != right_props[key]
    ]
    return {
        "antes": {"arquivo": before["arquivo"], "sha256": before["sha256"]},
        "depois": {"arquivo": after["arquivo"], "sha256": after["sha256"]},
        "resumo": {
            "adicionados": len(added),
            "removidos": len(removed),
            "movidos_ou_renomeados": len(moved),
            "propriedades_selecionadas_alteradas": len(changed),
        },
        "adicionados": added,
        "removidos": removed,
        "movidos_ou_renomeados": moved,
        "propriedades_alteradas": changed,
        "limite": (
            "Comparação parcial por GUID/caminho e propriedades selecionadas. "
            "Bibliotecas, scripts, geometria e vínculos indiretos exigem revisão adicional."
        ),
    }
