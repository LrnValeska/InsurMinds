# InsurMinds

## Plataforma Inteligente para Análise e Comparação de Apólices D&O

O **InsurMinds** é uma aplicação baseada em Inteligência Artificial Generativa desenvolvida para auxiliar na análise e comparação de apólices de seguro **Directors & Officers (D&O)**.

A solução permite que o usuário envie duas apólices em formato PDF e obtenha automaticamente informações relevantes dos documentos, como seguradora, segurado, vigência, limite máximo de indenização, franquia, coberturas, exclusões, retroatividade e âmbito territorial.

O projeto utiliza um fluxo de processamento que combina **extração de documentos, processamento estruturado de informações e Inteligência Artificial Generativa**, buscando reduzir o trabalho manual necessário para localizar e organizar informações presentes em documentos de seguros.

> **Status:** MVP funcional em desenvolvimento.

---

## Objetivo

O objetivo do InsurMinds é desenvolver um protótipo funcional capaz de:

- receber apólices de seguro em PDF;
- extrair automaticamente o conteúdo dos documentos;
- identificar informações relevantes de apólices D&O;
- estruturar os dados extraídos;
- utilizar Inteligência Artificial Generativa para interpretar os documentos;
- comparar diferentes apólices;
- apresentar as informações de forma organizada;
- auxiliar o usuário na análise das diferenças entre documentos.

A proposta é demonstrar como técnicas de IA Generativa podem ser aplicadas à análise de documentos do mercado de seguros.

---

## Como funciona

O fluxo principal da aplicação é:

```text
                  ┌─────────────────────┐
                  │   Upload dos PDFs   │
                  │    Apólice A + B    │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Extração de texto   │
                  │      PyMuPDF        │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Agente de análise   │
                  │       D&O           │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │    Gemini API       │
                  │   IA Generativa     │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Dados estruturados  │
                  │      Pydantic       │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Interface Streamlit │
                  └─────────────────────┘
