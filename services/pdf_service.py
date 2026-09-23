import pymupdf


def extrair_texto_pdf(arquivo_pdf):
    """
    Extrai o texto de cada página de um PDF.
    """

    arquivo_bytes = arquivo_pdf.read()

    documento = pymupdf.open(
        stream=arquivo_bytes,
        filetype="pdf"
    )

    paginas = []

    for numero_pagina, pagina in enumerate(documento, start=1):

        texto = pagina.get_text("text")

        paginas.append({
            "pagina": numero_pagina,
            "texto": texto
        })

    resultado = {
        "nome": arquivo_pdf.name,
        "total_paginas": len(documento),
        "paginas": paginas
    }

    documento.close()

    return resultado


def juntar_texto_paginas(resultado_pdf):
    """
    Junta todas as páginas preservando
    a indicação do número da página.
    """

    textos = []

    for pagina in resultado_pdf["paginas"]:

        textos.append(
            f"\n--- PÁGINA {pagina['pagina']} ---\n"
            f"{pagina['texto']}"
        )

    return "\n".join(textos)