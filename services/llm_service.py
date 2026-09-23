import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY não encontrada. "
        "Verifique o arquivo .env."
    )


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def gerar_resposta(prompt):
    """
    Envia um prompt ao Gemini.

    Primeiro tenta Gemini 3.6 Flash.
    Se houver indisponibilidade temporária,
    tenta novamente e depois utiliza o Flash-Lite.
    """

    modelos = [
        "gemini-3.6-flash",
        "gemini-3.5-flash-lite"
    ]

    ultimo_erro = None

    for modelo in modelos:

        for tentativa in range(2):

            try:

                resposta = client.models.generate_content(
                    model=modelo,
                    contents=prompt
                )

                if resposta.text:
                    return resposta.text

            except Exception as erro:

                ultimo_erro = erro

                mensagem = str(erro)

                # Erro temporário de alta demanda
                if (
                    "503" in mensagem
                    or "UNAVAILABLE" in mensagem
                    or "high demand" in mensagem
                ):

                    time.sleep(2)
                    continue

                # Outro tipo de erro
                raise erro

    raise RuntimeError(
        "Os modelos Gemini estão temporariamente "
        "indisponíveis. Tente novamente em alguns minutos. "
        f"Detalhes: {ultimo_erro}"
    )