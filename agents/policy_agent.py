import json

from services.llm_service import gerar_resposta
from models.policy import ApoliceDO


def analisar_apolice(texto):
    """
    Analisa uma apólice D&O utilizando o Gemini
    e transforma o resultado em dados estruturados.
    """

    prompt = f"""
Você é um agente especializado em análise de apólices
de seguro D&O (Directors and Officers).

Analise exclusivamente o documento fornecido abaixo.

Extraia:

- seguradora
- segurado/tomador
- número da apólice
- início da vigência
- fim da vigência
- limite máximo de indenização
- franquia
- coberturas
- exclusões
- retroatividade
- âmbito territorial

REGRAS:

1. Não invente informações.
2. Utilize somente informações presentes no documento.
3. Se uma informação não existir, utilize null.
4. Coberturas devem ser uma lista.
5. Exclusões devem ser uma lista.
6. Retorne somente JSON válido.
7. Não utilize Markdown.

Retorne exatamente esta estrutura:

{{
    "seguradora": null,
    "segurado_tomador": null,
    "numero_apolice": null,
    "inicio_vigencia": null,
    "fim_vigencia": null,
    "limite_maximo_indenizacao": null,
    "franquia": null,
    "coberturas": [],
    "exclusoes": [],
    "retroatividade": null,
    "ambito_territorial": null
}}

DOCUMENTO:

{texto}
"""

    resposta = gerar_resposta(prompt)

    resposta = resposta.strip()

    if resposta.startswith("```json"):
        resposta = resposta[7:]

    if resposta.startswith("```"):
        resposta = resposta[3:]

    if resposta.endswith("```"):
        resposta = resposta[:-3]

    dados = json.loads(resposta.strip())

    return ApoliceDO(**dados)