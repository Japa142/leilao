import streamlit as st
import datetime

def main():
    st.set_page_config(page_title="Checklist Super Completo - Leilão de Imóveis", layout="wide")
    st.title("Checklist Super Completo para Compra de Imóveis em Leilão - Goiás")

    st.write("""
    Este aplicativo foi criado para **guiar você em passos detalhados** para a compra de imóveis
    em leilão (judicial ou extrajudicial), abarcando **todas** as principais cautelas:

    - Definição de objetivo e orçamento.
    - Seleção e análise de valor de mercado (conversar com corretores, pesquisa in loco).
    - Verificações de documentação, edital e notificação do antigo dono (extrajudicial).
    - Ocupação do imóvel (desocupado ou com acordo amigável).
    - Formas de pagamento (à vista, financiamento pela Caixa).
    - Cálculo de custos (lance, comissão, ITBI, registro, dívidas passadas, reforma).
    - Planejamento de reforma (o que compensa reformar).
    - Resumo final de todos os gastos até a **revenda** (se for para investimento).

    No final, gere um **Relatório Completo** com todas as informações e custos estimados.
    """)

    # ---------------------------------------------------------------------------------
    # DADOS INICIAIS
    # ---------------------------------------------------------------------------------
    data_hoje = datetime.date.today().strftime("%d/%m/%Y")
    st.sidebar.subheader("Dados Iniciais")
    nome_comprador = st.sidebar.text_input("Seu nome (Pessoa Física):", "")
    data_atual = st.sidebar.text_input("Data:", data_hoje)

    st.sidebar.write("---")
    st.sidebar.markdown("### Passos Principais:")
    st.sidebar.markdown("1. Objetivos e Orçamento")
    st.sidebar.markdown("2. Análise de Mercado (Corretores, Valor)")
    st.sidebar.markdown("3. Verificação de Documentação (Edital, Notificações)")
    st.sidebar.markdown("4. Situação de Ocupação")
    st.sidebar.markdown("5. Forma de Pagamento")
    st.sidebar.markdown("6. Cálculo de Custos do Leilão")
    st.sidebar.markdown("7. Planejamento de Reforma")
    st.sidebar.markdown("8. Resumo Final")

    st.write(f"**Data atual:** {data_atual}")
    if nome_comprador:
        st.write(f"**Nome do comprador:** {nome_comprador}")
    else:
        st.write("*(Insira o nome na barra lateral para personalizar o checklist)*")

    st.markdown("---")

    # =================================================================================
    # PASSO 1: OBJETIVO E ORÇAMENTO
    # =================================================================================
    st.header("PASSO 1: Definir Objetivo e Orçamento")
    st.write("""
    **PASSO 1.1** - Escolha o objetivo principal:
    - Moradia Própria
    - Investimento (revenda/locação)
    - Outros
    """)

    objetivo = st.selectbox(
        "Seu principal objetivo:",
        ["(Selecione)", "Moradia Própria", "Investimento (Revenda/Locação)", "Outros"]
    )

    st.write("""
    **PASSO 1.2** - Defina seu **orçamento total máximo**, incluindo:
    - Valor de arrematação (lance)
    - Comissão do leiloeiro
    - Custos de cartório, ITBI
    - Possíveis dívidas de IPTU/condomínio
    - Custo de reforma
    - Outros custos adicionais
    """)

    valor_orcamento_max = st.number_input(
        "Orçamento máximo (R$)", min_value=0.0, step=10000.0, format="%.2f"
    )

    # =================================================================================
    # PASSO 2: ANÁLISE DE MERCADO (CONVERSAR COM CORRETORES, ETC.)
    # =================================================================================
    st.header("PASSO 2: Análise de Mercado e Seleção do Imóvel")
    st.write("""
    **PASSO 2.1** - Verifique o **local** do imóvel (cidade/bairro em Goiás) e **tipo**:
    """)

    local_imovel = st.text_input("Cidade/Bairro do imóvel em Goiás:", "")
    tipo_imovel = st.radio("Tipo de Imóvel:", ["Casa", "Apartamento"])

    st.write("""
    **PASSO 2.2** - **Conversar com corretores** locais e/ou pesquisar em portais imobiliários 
    para estimar o valor de mercado de imóveis semelhantes na região.
    """)

    consultou_corretores = st.checkbox("Conversei com corretores para ter preço médio da região?")
    pesquisa_portais = st.checkbox("Pesquisei portais imobiliários (Ex: Zap, OLX, Viva Real) para comparar?")

    st.write("""
    **PASSO 2.3** - Determine o **valor de mercado estimado** do imóvel com base nessas informações:
    """)

    valor_mercado = st.number_input(
        "Valor de mercado estimado (R$):", min_value=0.0, step=10000.0, format="%.2f"
    )

    st.write("""
    **PASSO 2.4** - Se possível, **visite presencialmente** o imóvel para avaliar 
    estado de conservação, vizinhança, segurança, etc.
    """)

    visitou = st.checkbox("Visitei o imóvel (ou pretendo visitar antes do leilão)?")

    # =================================================================================
    # PASSO 3: VERIFICAÇÃO DE DOCUMENTAÇÃO (EDITAL, NOTIFICAÇÃO, ETC.)
    # =================================================================================
    st.header("PASSO 3: Verificar Documentação, Edital e Notificações")
    st.write("""
    **PASSO 3.1** - Ler **edital** para saber:
    1. Se é Leilão Judicial (1ª e 2ª praça) ou Extrajudicial (Alienação Fiduciária).
    2. Valor mínimo, incrementos, datas.
    3. Formas de pagamento (à vista, parcelado, financiamento).
    4. Responsabilidade por dívidas (IPTU, condomínio).
    5. Comissão do leiloeiro (geralmente 5%).
    """)

    tipo_leilao = st.radio("Tipo de Leilão:", ["Judicial", "Extrajudicial"], index=0)
    edital_lido = st.checkbox("Li o edital e compreendi todas as regras.")

    st.write("""
    **PASSO 3.2** - Obter a **Matrícula do imóvel** (certidão de inteiro teor) no 
    Cartório de Registro de Imóveis para conferir:
    - Proprietário atual
    - Existência de penhoras, hipotecas, usufrutos
    - Consolidação da propriedade (caso extrajudicial)
    - Averbação de penhora (caso judicial)
    """)

    matricula_conf = st.checkbox("Verifiquei a matrícula atualizada no Cartório.")

    st.write("""
    **PASSO 3.3** - **Se for Leilão Extrajudicial**: verifique se houve **notificação correta** do devedor 
    para purgar a mora, conforme a Lei 9.514/97. Falhas na notificação podem acarretar 
    nulidade do leilão no futuro.
    """)

    # Só mostra se for extrajudicial
    notificacao = "Não se aplica (Leilão Judicial)"
    if tipo_leilao == "Extrajudicial":
        notificacao_check = st.checkbox("Confirmei que o antigo dono foi notificado conforme a lei (ok na matrícula).")
        notificacao = "Sim" if notificacao_check else "Não (ou não verificado)"

    # =================================================================================
    # PASSO 4: SITUAÇÃO DE OCUPAÇÃO
    # =================================================================================
    st.header("PASSO 4: Verificar Ocupação do Imóvel")
    st.write("""
    **Verifique se o imóvel está desocupado ou se existe algum morador (ex-proprietário, inquilino):**

    - Se **desocupado**, posse é mais simples.
    - Se **ocupado**:
      - Tentar acordo amigável (indemnização, prazo para sair).
      - Se o ocupante se recusa, talvez seja melhor **não** arrematar para evitar longas disputas 
        (a menos que esteja disposto a encarar uma ação de imissão na posse).
    """)

    ocupado = st.radio("O imóvel está ocupado?", ["Não", "Sim"], index=0)
    acordo_amigavel = "Não se aplica"
    valor_acordo = 0.0

    if ocupado == "Sim":
        acordo_amigavel = st.radio("Há possibilidade de acordo amigável para desocupação?", ["Sim", "Não"], index=1)
        if acordo_amigavel == "Sim":
            valor_acordo = st.number_input(
                "Valor previsto de compensação (auxílio mudança, etc.)",
                min_value=0.0, step=1000.0, format="%.2f"
            )

    # =================================================================================
    # PASSO 5: FORMA DE PAGAMENTO (À VISTA / FINANCIAMENTO)
    # =================================================================================
    st.header("PASSO 5: Definir Forma de Pagamento")
    st.write("""
    - **Leilão Judicial** pode ser pago à vista ou em até 30 parcelas (CPC art. 895), 
      com 25% de entrada. 
    - **Leilão Extrajudicial** (bancos) muitas vezes permite **financiamento** (ex.: Caixa), 
      usando FGTS se atender requisitos.
    """)

    forma_pagamento = st.radio("Forma de Pagamento:", ["À Vista", "Financiamento Caixa"], index=0)

    perc_entrada = 0.0
    if forma_pagamento == "Financiamento Caixa":
        st.write("""
        **Financiamento** na Caixa geralmente exige uma entrada (20-30% ou mais).  
        O restante é financiado, podendo usar FGTS.
        """)
        perc_entrada = st.number_input(
            "Percentual de entrada (%)", min_value=5.0, max_value=90.0, step=5.0, value=25.0,
            format="%.1f"
        )

    # =================================================================================
    # PASSO 6: CÁLCULO DE CUSTOS DO LEILÃO
    # =================================================================================
    st.header("PASSO 6: Calcular Custos Principais do Leilão")
    st.write("""
    **6.1. Valor do Lance (arrematação)**  
    Defina um valor provável de arrematação. Se ainda não sabe exatamente, use um valor aproximado.
    """)

    valor_lance = st.number_input("Valor de arrematação (R$):", min_value=0.0, step=10000.0, format="%.2f")

    st.write("""
    **6.2. Comissão do Leiloeiro**  
    Geralmente 5% do valor do lance.
    """)
    comissao_leiloeiro = valor_lance * 0.05

    st.write("""
    **6.3. ITBI**  
    Geralmente entre 2% e 3% em muitos municípios. Ajuste conforme a sua cidade em Goiás.
    """)
    perc_itbi = st.slider("Porcentagem de ITBI (%)", 1.0, 5.0, 2.5, 0.5)
    itbi = valor_lance * (perc_itbi / 100.0)

    st.write("""
    **6.4. Registro em Cartório**  
    Em média 1% a 1,5% do valor do imóvel; pode variar.
    """)
    perc_registro = st.slider("Porcentagem de Registro (%)", 0.5, 2.0, 1.2, 0.1)
    registro_cartorio = valor_lance * (perc_registro / 100.0)

    st.write("""
    **6.5. Dívidas de IPTU / Condomínio**  
    Se o edital não isenta ou se não forem pagos pelo banco (em extrajudiciais da Caixa, às vezes eles pagam). 
    """)
    debitos_passados = st.number_input("Estimativa de dívidas (IPTU/condomínio) (R$)", min_value=0.0, step=1000.0, format="%.2f")

    # Soma parcial
    custo_aquisicao_bruto = valor_lance + comissao_leiloeiro + itbi + registro_cartorio + debitos_passados + valor_acordo

    # =================================================================================
    # PASSO 7: PLANEJAMENTO DE REFORMA
    # =================================================================================
    st.header("PASSO 7: Planejamento de Reforma")
    st.write("""
    **Liste as principais áreas que pretende reformar** e estime o custo total.  
    Exemplos:  
    - Reparos estruturais (telhado, laje, fundações)  
    - Elétrica e hidráulica  
    - Revestimentos, pintura, esquadrias  
    - Banheiros e cozinha (modernização)  
    - Paisagismo ou fachada (se for casa)

    Defina um **valor total estimado** para reforma:
    """)

    custo_reforma = st.number_input("Custo total de reforma (R$):", min_value=0.0, step=1000.0, format="%.2f")

    # =================================================================================
    # CÁLCULO FINAL / PASSO 8
    # =================================================================================
    st.header("PASSO 8: Resumo Final")
    investimento_total = custo_aquisicao_bruto + custo_reforma

    # Se financiamento, calcular entrada e saldo
    valor_entrada = 0.0
    valor_financiado = 0.0
    if forma_pagamento == "Financiamento Caixa":
        valor_entrada = valor_lance * (perc_entrada / 100.0)
        valor_financiado = max(valor_lance - valor_entrada, 0.0)

    # BOTÃO PARA GERAR RELATÓRIO
    if st.button("Gerar Relatório Completo"):
        st.subheader("RELATÓRIO COMPLETO DO CHECKLIST")
        st.write(f"**Data:** {data_atual}")
        if nome_comprador:
            st.write(f"**Nome do Comprador:** {nome_comprador}")

        st.write("---")
        st.write("### Passo 1: Objetivo e Orçamento")
        st.write(f"- Objetivo: {objetivo}")
        st.write(f"- Orçamento Máximo: R$ {valor_orcamento_max:,.2f}")

        st.write("### Passo 2: Análise de Mercado")
        st.write(f"- Local (GO): {local_imovel}")
        st.write(f"- Tipo de Imóvel: {tipo_imovel}")
        st.write(f"- Consultou Corretores? {'Sim' if consultou_corretores else 'Não'}")
        st.write(f"- Pesquisa em Portais? {'Sim' if pesquisa_portais else 'Não'}")
        st.write(f"- Valor de Mercado Estimado: R$ {valor_mercado:,.2f}")
        st.write(f"- Visita In Loco? {'Sim' if visitou else 'Não'}")

        st.write("### Passo 3: Documentação")
        st.write(f"- Tipo de Leilão: {tipo_leilao}")
        st.write(f"- Edital lido? {'Sim' if edital_lido else 'Não'}")
        st.write(f"- Matrícula verificada? {'Sim' if matricula_conf else 'Não'}")
        if tipo_leilao == "Extrajudicial":
            st.write(f"- Antigo dono notificado corretamente? {notificacao}")

        st.write("### Passo 4: Ocupação")
        st.write(f"- Ocupado? {ocupado}")
        if ocupado == "Sim":
            st.write(f"  - Acordo amigável? {acordo_amigavel}")
            if acordo_amigavel == "Sim":
                st.write(f"  - Valor de acordo (auxílio): R$ {valor_acordo:,.2f}")

        st.write("### Passo 5: Forma de Pagamento")
        st.write(f"- Forma: {forma_pagamento}")
        if forma_pagamento == "Financiamento Caixa":
            st.write(f"  - Percentual de entrada: {perc_entrada}%")
            st.write(f"  - Valor de entrada (aprox.): R$ {valor_entrada:,.2f}")
            st.write(f"  - Valor financiado (aprox.): R$ {valor_financiado:,.2f}")

        st.write("### Passo 6: Custos de Aquisição")
        st.write(f"- Lance (arrematação): R$ {valor_lance:,.2f}")
        st.write(f"- Comissão do Leiloeiro (5%): R$ {comissao_leiloeiro:,.2f}")
        st.write(f"- ITBI ({perc_itbi}%): R$ {itbi:,.2f}")
        st.write(f"- Registro em Cartório ({perc_registro}%): R$ {registro_cartorio:,.2f}")
        st.write(f"- Dívidas Passadas (IPTU/condomínio): R$ {debitos_passados:,.2f}")
        if valor_acordo > 0:
            st.write(f"- Acordo de Desocupação: R$ {valor_acordo:,.2f}")
        st.write(f"**Subtotal de Aquisição**: R$ {custo_aquisicao_bruto:,.2f}")

        st.write("### Passo 7: Reforma")
        st.write(f"- Custo Total de Reforma: R$ {custo_reforma:,.2f}")

        st.write("### Passo 8: Total Geral do Investimento")
        st.write(f"**Investimento (Compra + Reforma)**: R$ {investimento_total:,.2f}")

        st.write("---")
        st.success("""
        **Checklist Finalizado!**  
        Este relatório consolida todas as etapas e estimativas de custo.  
        Lembre-se de ajustar valores conforme orçamentos reais e legislação local.  
        """)

# -------------------------------------------------------------------------------------
# EXECUÇÃO
# -------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
