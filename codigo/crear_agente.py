"""Lab 6 — Crea por código el agente "asesor-moda-andina" con File Search sobre los documentos del taller.

Requisitos:  pip install -r requirements.txt   y   az login  (con la cuenta del taller)
Variables:   FOUNDRY_PROJECT_ENDPOINT = https://<recurso>.services.ai.azure.com/api/projects/<proyecto>
             FOUNDRY_MODEL_NAME       = nombre del despliegue, p. ej. gpt-5.4-mini
             AGENT_NAME               = (opcional) asesor-moda-andina-<alias>
"""
import os
from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FileSearchTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential

DATOS = Path(__file__).resolve().parent.parent / "datos_taller"
DOCS = ["politica_cambios_y_devoluciones.md", "guia_de_tallas.md", "catalogo_coleccion_temporada.md"]
AGENT_NAME = os.environ.get("AGENT_NAME", "asesor-moda-andina")

INSTRUCCIONES = """Eres el asesor virtual de Moda Andina, una marca de ropa (ficticia).
- Responde en español, con tono cercano y frases cortas.
- Usa SOLO la información de los documentos (políticas, guía de tallas y catálogo). Si no está, dilo y sugiere los canales de atención.
- Cuando recomiendes prendas, incluye la referencia y el precio, y sugiere con qué combinarla.
- Para tallas, pide las medidas si el cliente no las da.
- No respondas temas ajenos a la tienda; redirige amablemente."""

with (
    DefaultAzureCredential() as cred,
    AIProjectClient(endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"], credential=cred) as project,
    project.get_openai_client() as openai,
):
    vs = openai.vector_stores.create(name=f"docs-{AGENT_NAME}")
    for name in DOCS:
        with open(DATOS / name, "rb") as f:
            openai.vector_stores.files.upload_and_poll(vector_store_id=vs.id, file=f)
    print(f"Vector store {vs.id} con {len(DOCS)} documentos")

    agent = project.agents.create_version(
        agent_name=AGENT_NAME,
        definition=PromptAgentDefinition(
            model=os.environ["FOUNDRY_MODEL_NAME"],
            instructions=INSTRUCCIONES,
            tools=[FileSearchTool(vector_store_ids=[vs.id])],
        ),
        description="Asesor de tienda del taller Microsoft Foundry",
    )
    print(f"Agente creado: {agent.name} (versión {agent.version})")
