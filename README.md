# Taller Microsoft Foundry: IA generativa y agentes en Azure

Material del taller de **Microsoft Foundry** (antes *Azure AI Foundry*) dictado por **GoToCloud** para **Permoda (KOAJ)**.
Duración: 4 horas, con un bloque teórico y un laboratorio práctico de ~100 minutos.

> ⚠️ Los documentos y datos de `datos_taller/` son **ficticios** (marca inventada "Moda Andina"). Se crearon solo para el taller y no corresponden a políticas, precios ni cifras reales de Permoda o KOAJ.

## Contenido

| Carpeta / archivo | Qué es |
|---|---|
| [`Guia_del_taller_practico.md`](Guia_del_taller_practico.md) | Guía paso a paso de los laboratorios 0 a 6 |
| [`presentacion/`](presentacion/) | Presentación del taller: teoría, casos de uso y resumen de laboratorios |
| [`datos_taller/`](datos_taller/) | Documentos y datos ficticios para los agentes y la evaluación |
| [`codigo/`](codigo/) | Scripts de Python para crear un agente y conversar con él usando el SDK de Foundry |

## Agenda

| Hora | Bloque |
|---|---|
| 0:00 | Bienvenida y verificación de acceso |
| 0:15 | Fundamentos de IA generativa |
| 0:30 | Microsoft Foundry: plataforma y modelos |
| 1:00 | Agentes, conocimiento y herramientas |
| 1:25 | Evaluación, seguridad y gobierno |
| 1:45 | Receso |
| 1:55 | Casos de uso para Permoda |
| 2:05 | Taller práctico (laboratorios 0 a 6) |
| 3:45 | Cierre y próximos pasos |

## Laboratorios

0. **Ingreso y verificación:** acceso al tenant y al grupo de recursos del taller.
1. **Recurso y proyecto:** crear tu recurso Foundry y tu proyecto.
2. **Modelo y playground:** desplegar `gpt-5.4-mini` y crear un redactor de e-commerce.
3. **Agente asesor de tienda:** File Search sobre políticas, guía de tallas y catálogo.
4. **Agente analista de ventas:** Code Interpreter con `ventas_tiendas_2025.csv`.
5. **Guardrails y evaluación:** seguridad de contenido y evaluación con `preguntas_evaluacion.jsonl`.
6. **Código (opcional):** usar el agente desde Python.

## Requisitos

- Cuenta con acceso al ambiente del taller. GoToCloud la entrega antes de la sesión como invitado B2B.
- Microsoft Authenticator para MFA.
- Navegador Edge o Chrome actualizado.
- Solo para el Lab 6: Python 3.10+ y la [CLI de Azure](https://learn.microsoft.com/cli/azure/install-azure-cli).

## Uso rápido del código (Lab 6)

```powershell
cd codigo
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
az login --tenant <ID-del-tenant>
$env:FOUNDRY_PROJECT_ENDPOINT = "https://<recurso>.services.ai.azure.com/api/projects/<proyecto>"
$env:FOUNDRY_MODEL_NAME = "gpt-5.4-mini"
$env:AGENT_NAME = "asesor-<alias>"
python crear_agente.py       # opcional: crea el agente por código
python conversar_agente.py   # chat por consola con el agente
```

El instructor comparte el ID del tenant durante la sesión. Los scripts funcionan en cualquier proyecto de Microsoft Foundry: solo cambia el endpoint y el nombre del despliegue.

## Recursos

- Documentación de Microsoft Foundry: https://learn.microsoft.com/azure/foundry
- Microsoft Learn: https://learn.microsoft.com/training
- Ejemplos del SDK: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-projects/samples

---
Material preparado por [GoToCloud](https://www.gotocloud.in).
