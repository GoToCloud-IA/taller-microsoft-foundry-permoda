"""Lab 6 — Conversa desde código con un agente de Foundry (el creado en el portal o con crear_agente.py).

Uso:  python conversar_agente.py                    -> chat interactivo (escribe 'salir' para terminar)
      python conversar_agente.py "pregunta 1" "..."  -> envía las preguntas en la misma conversación
Variables: FOUNDRY_PROJECT_ENDPOINT, AGENT_NAME
"""
import os
import sys

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

AGENT = {"agent_reference": {"name": os.environ.get("AGENT_NAME", "asesor-moda-andina"), "type": "agent_reference"}}

with (
    DefaultAzureCredential() as cred,
    AIProjectClient(endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"], credential=cred) as project,
    project.get_openai_client() as openai,
):
    conversation = openai.conversations.create()  # mantiene el contexto entre preguntas
    preguntas = iter(sys.argv[1:]) if len(sys.argv) > 1 else iter(lambda: input("\nTú: "), "salir")
    for pregunta in preguntas:
        r = openai.responses.create(conversation=conversation.id, input=pregunta, extra_body=AGENT)
        print(f"\nTú: {pregunta}\nAgente: {r.output_text}\n  [tokens: {r.usage.input_tokens} entrada / {r.usage.output_tokens} salida]")
