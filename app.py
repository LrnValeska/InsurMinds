import streamlit as st

from services.pdf_service import (
    extrair_texto_pdf,
    juntar_texto_paginas
)

from agents.policy_agent import analisar_apolice


# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="InsurMinds",
    page_icon="📄",
    layout="wide"
)

st.title("InsurMinds")

st.subheader(
    "Plataforma Inteligente para Análise e Comparação de Apólices D&O"
)

st.write(
    "Envie duas apólices para extrair, analisar e comparar "
    "automaticamente suas informações."
)

st.divider()


# =========================================================
# UPLOAD
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown("### Apólice A")

    apolice_a = st.file_uploader(
        "Selecione a primeira apólice",
        type=["pdf"],
        key="apolice_a"
    )

    if apolice_a:
        st.success(
            f"Arquivo carregado: {apolice_a.name}"
        )


with col2:

    st.markdown("### Apólice B")

    apolice_b = st.file_uploader(
        "Selecione a segunda apólice",
        type=["pdf"],
        key="apolice_b"
    )

    if apolice_b:
        st.success(
            f"Arquivo carregado: {apolice_b.name}"
        )


st.divider()


# =========================================================
# PROCESSAMENTO
# =========================================================

if st.button(
    "Analisar apólices com IA",
    type="primary",
    use_container_width=True
):

    if apolice_a is None or apolice_b is None:

        st.warning(
            "Envie duas apólices antes de iniciar a análise."
        )

    else:

        try:

            # ---------------------------------------------
            # ETAPA 1 - EXTRAÇÃO DOS PDFs
            # ---------------------------------------------

            with st.spinner(
                "Extraindo conteúdo das apólices..."
            ):

                resultado_a = extrair_texto_pdf(
                    apolice_a
                )

                resultado_b = extrair_texto_pdf(
                    apolice_b
                )

                st.session_state[
                    "resultado_a"
                ] = resultado_a

                st.session_state[
                    "resultado_b"
                ] = resultado_b


            # ---------------------------------------------
            # ETAPA 2 - JUNTA O TEXTO DAS PÁGINAS
            # ---------------------------------------------

            texto_a = juntar_texto_paginas(
                resultado_a
            )

            texto_b = juntar_texto_paginas(
                resultado_b
            )


            # ---------------------------------------------
            # ETAPA 3 - GEMINI
            # ---------------------------------------------

            with st.spinner(
                "A Inteligência Artificial está analisando "
                "as apólices..."
            ):

                analise_a = analisar_apolice(
                    texto_a
                )

                analise_b = analisar_apolice(
                    texto_b
                )


            # ---------------------------------------------
            # SALVA RESULTADOS
            # ---------------------------------------------

            st.session_state[
                "analise_a"
            ] = analise_a

            st.session_state[
                "analise_b"
            ] = analise_b

            st.success(
                "Análise concluída com sucesso!"
            )


        except Exception as erro:

            st.error(
                f"Erro durante o processamento: {erro}"
            )


# =========================================================
# RESULTADO DA IA
# =========================================================

if (
    "analise_a" in st.session_state
    and
    "analise_b" in st.session_state
):

    analise_a = st.session_state[
        "analise_a"
    ]

    analise_b = st.session_state[
        "analise_b"
    ]

    st.divider()

    st.header(
        "Análise por Inteligência Artificial"
    )


    # -----------------------------------------------------
    # INFORMAÇÕES PRINCIPAIS
    # -----------------------------------------------------

    col1, col2 = st.columns(2)


    # APÓLICE A

    with col1:

        st.subheader("Apólice A")

        st.write(
            "**Seguradora:**",
            analise_a.seguradora or "Não identificado"
        )

        st.write(
            "**Segurado/Tomador:**",
            analise_a.segurado_tomador
            or "Não identificado"
        )

        st.write(
            "**Número da apólice:**",
            analise_a.numero_apolice
            or "Não identificado"
        )

        st.write(
            "**Início da vigência:**",
            analise_a.inicio_vigencia
            or "Não identificado"
        )

        st.write(
            "**Fim da vigência:**",
            analise_a.fim_vigencia
            or "Não identificado"
        )

        st.write(
            "**Limite máximo de indenização:**",
            analise_a.limite_maximo_indenizacao
            or "Não identificado"
        )

        st.write(
            "**Franquia:**",
            analise_a.franquia
            or "Não identificado"
        )

        st.write(
            "**Retroatividade:**",
            analise_a.retroatividade
            or "Não identificado"
        )

        st.write(
            "**Âmbito territorial:**",
            analise_a.ambito_territorial
            or "Não identificado"
        )

        st.markdown("#### Coberturas")

        if analise_a.coberturas:

            for cobertura in analise_a.coberturas:
                st.write(
                    f"• {cobertura}"
                )

        else:

            st.write(
                "Nenhuma cobertura identificada."
            )


        st.markdown("#### Exclusões")

        if analise_a.exclusoes:

            for exclusao in analise_a.exclusoes:
                st.write(
                    f"• {exclusao}"
                )

        else:

            st.write(
                "Nenhuma exclusão identificada."
            )


    # APÓLICE B

    with col2:

        st.subheader("Apólice B")

        st.write(
            "**Seguradora:**",
            analise_b.seguradora or "Não identificado"
        )

        st.write(
            "**Segurado/Tomador:**",
            analise_b.segurado_tomador
            or "Não identificado"
        )

        st.write(
            "**Número da apólice:**",
            analise_b.numero_apolice
            or "Não identificado"
        )

        st.write(
            "**Início da vigência:**",
            analise_b.inicio_vigencia
            or "Não identificado"
        )

        st.write(
            "**Fim da vigência:**",
            analise_b.fim_vigencia
            or "Não identificado"
        )

        st.write(
            "**Limite máximo de indenização:**",
            analise_b.limite_maximo_indenizacao
            or "Não identificado"
        )

        st.write(
            "**Franquia:**",
            analise_b.franquia
            or "Não identificado"
        )

        st.write(
            "**Retroatividade:**",
            analise_b.retroatividade
            or "Não identificado"
        )

        st.write(
            "**Âmbito territorial:**",
            analise_b.ambito_territorial
            or "Não identificado"
        )

        st.markdown("#### Coberturas")

        if analise_b.coberturas:

            for cobertura in analise_b.coberturas:
                st.write(
                    f"• {cobertura}"
                )

        else:

            st.write(
                "Nenhuma cobertura identificada."
            )


        st.markdown("#### Exclusões")

        if analise_b.exclusoes:

            for exclusao in analise_b.exclusoes:
                st.write(
                    f"• {exclusao}"
                )

        else:

            st.write(
                "Nenhuma exclusão identificada."
            )


# =========================================================
# TEXTO ORIGINAL EXTRAÍDO
# =========================================================

if (
    "resultado_a" in st.session_state
    and
    "resultado_b" in st.session_state
):

    resultado_a = st.session_state[
        "resultado_a"
    ]

    resultado_b = st.session_state[
        "resultado_b"
    ]

    st.divider()

    with st.expander(
        "Ver conteúdo original extraído dos PDFs"
    ):

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Apólice A")

            st.caption(
                f"{resultado_a['total_paginas']} página(s)"
            )

            for pagina in resultado_a["paginas"]:

                st.markdown(
                    f"**Página {pagina['pagina']}**"
                )

                st.text(
                    pagina["texto"][:3000]
                )


        with col2:

            st.subheader("Apólice B")

            st.caption(
                f"{resultado_b['total_paginas']} página(s)"
            )

            for pagina in resultado_b["paginas"]:

                st.markdown(
                    f"**Página {pagina['pagina']}**"
                )

                st.text(
                    pagina["texto"][:3000]
                )