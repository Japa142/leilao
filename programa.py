import streamlit as st
import datetime

# Função auxiliar para formatar valores em estilo brasileiro, ex: 120.000,00
def format_brl(value: float) -> str:
    """
    Formata valor float no estilo brasileiro: 1.234.567,89
    """
    if value is None:
        return ""
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def main():
    st.set_page_config(page_title="Checklist Passo a Passo - Leilão Imóveis", layout="wide")
    st.title("Checklist Completo (Passo a Passo) para Comprar e Revender Imóvel em Leilão")

    st.write("""
    Este aplicativo apresenta **passos detalhados** para adquirir um imóvel em leilão (judicial ou extrajudicial)
    no estado de Goiás, com possibilidade de **financiamento** (ex.: Caixa), englobando:
    - Verificações e cuidados (visita, notificação, documentação).
    - Cadastro no site do leiloeiro, participação e arrematação.
    - Pagamentos (lance, comissão, ITBI, registro em cartório).
    - Planejamento de reforma e revenda.
    """)

    # DADOS INICIAIS (BARRA LATERAL)
    data_hoje = datetime.date.today().strftime("%d/%m/%Y")
    st.sidebar.subheader("Dados Iniciais")
    nome_comprador = st.sidebar.text_input("Seu nome (Pessoa Física):", "")
    data_atual = st.sidebar.text_input("Data:", data_hoje)

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Etapas:")
    st.sidebar.markdown("1. Objetivos e Habilitação")
    st.sidebar.markdown("2. Visitar o Imóvel e Analisar Mercado")
    st.sidebar.markdown("3. Verificar Documentos e Edital")
    st.sidebar.markdown("4. Cadastro no Site e Participação no Leilão")
    st.sidebar.markdown("5. Forma de Pagamento e Custos Principais")
    st.sidebar.markdown("6. Pagamentos e Pós-Arremate")
    st.sidebar.markdown("7. Reforma e Venda")
    st.sidebar.markdown("8. Resumo Final")

    st.write(f"**Data atual:** {data_atual}")
    if nome_comprador:
        st.write(f"**Nome do comprador:** {nome_comprador}")
    else:
        st.write("*Preencha o nome na barra lateral para personalizar.*")

    st.markdown("---")

    # ================================================================
    # PASSO 1: DEFINIR OBJETIVOS E HABILITAR FINANCIAMENTO (SE PRECISO)
    # ================================================================
    st.header("PASSO 1: Definir Objetivos e Habilitação para Financiamento")

    objetivo = st.selectbox(
        "1.1 Qual seu principal objetivo?",
        ["(Selecione)", "Moradia Própria", "Investimento (Revenda/Locação)", "Outros"],
        help="Selecione se o imóvel é para você morar ou para gerar lucro, pois isso afeta seu planejamento."
    )

    st.write("1.2 Verifique se você **pode** financiar no nome que pretende (caso deseje financiamento).")
    financiamento_pre = st.checkbox(
        "Verifiquei se tenho aprovação prévia (ou vou buscar) para financiamento no meu nome?",
        help="Ex.: Consultar banco (Caixa) para saber se o comprador atende exigências, score, FGTS etc."
    )

    st.write("1.3 Defina seu **orçamento máximo** aproximado (compra + taxas + reforma).")
    valor_orcamento_max = st.number_input(
        "Orçamento máximo total (R$)",
        min_value=0.0, step=10000.0, format="%.2f",
        help="Inclua valor de lance + comissão + ITBI + registro + reforma + eventuais dívidas."
    )

    # ================================================================
    # PASSO 2: VISITAR IMÓVEL E ANALISAR MERCADO
    # ================================================================
    st.header("PASSO 2: Visitar o Imóvel e Analisar o Mercado")

    local_imovel = st.text_input(
        "2.1 Cidade/Bairro do imóvel em Goiás:",
        help="Ex.: Goiânia, Aparecida, Anápolis etc."
    )
    tipo_imovel = st.radio(
        "2.2 Tipo de Imóvel:",
        ["Casa", "Apartamento", "Outro"],
        help="Selecione de forma aproximada, ex.: Casa, Apê ou outro tipo."
    )

    visitou = st.checkbox(
        "2.3 Visitei (ou pretendo visitar) o imóvel pessoalmente?",
        help="Verifique a conservação, fale com vizinhos, síndico, porteiro etc."
    )

    st.write("2.4 Converse com corretores locais e faça pesquisa de mercado (sites, OLX, VivaReal).")
    conversou_corretores = st.checkbox(
        "Conversei com corretores sobre o valor médio da região?",
        help="É importante para não pagar acima do valor de mercado."
    )

    valor_mercado = st.number_input(
        "2.5 Valor de mercado estimado (R$):",
        min_value=0.0, step=10000.0, format="%.2f",
        help="Faça uma média do que encontrou nos portais e informações de corretores."
    )

    # ================================================================
    # PASSO 3: VERIFICAR DOCUMENTOS E EDITAL
    # ================================================================
    st.header("PASSO 3: Verificar Documentos, Edital e Notificações")

    tipo_leilao = st.radio(
        "3.1 Tipo de Leilão:",
        ["Judicial", "Extrajudicial"],
        help="Leilão Judicial: CPC art. 879+; Extrajudicial: Lei 9.514/97 (alienação fiduciária)."
    )

    edital_lido = st.checkbox(
        "3.2 Li o edital e entendi todas as regras?",
        help="Leia atentamente prazos, dívidas, comissão, formas de pagamento."
    )

    matricula_conf = st.checkbox(
        "3.3 Conferi a matrícula no Cartório de Registro de Imóveis?",
        help="Verifique titularidade, penhoras, se houve consolidação (extrajudicial) etc."
    )

    notificacao_ok = "Não se aplica"
    if tipo_leilao == "Extrajudicial":
        notificacao_ex = st.checkbox(
            "3.4 Verifiquei se o antigo dono foi notificado corretamente?",
            help="No extrajudicial, a falta de notificação pode anular o leilão."
        )
        notificacao_ok = "Sim" if notificacao_ex else "Não"

    # ================================================================
    # PASSO 4: CADASTRO NO SITE DO LEILOEIRO E PARTICIPAÇÃO
    # ================================================================
    st.header("PASSO 4: Cadastro no Site do Leiloeiro e Participação no Leilão")

    st.write("""
    4.1 É preciso se **cadastrar** (ou habilitar) no site do leiloeiro responsável.  
    - Envie documentos solicitados (RG, CPF, comprovante de residência).  
    - Algumas vezes é exigida caução (ex.: 5% do lance) para habilitar.
    """)

    cadastro_feito = st.checkbox(
        "Fiz (ou vou fazer) o cadastro no site/portal do leiloeiro?",
        help="Fundamental para poder dar lances, seja leilão online ou presencial."
    )

    st.write("""
    4.2 Verifique a **data e horário** do leilão. Programe-se e acompanhe possíveis adiamentos.  
    """)

    # ================================================================
    # PASSO 5: FORMA DE PAGAMENTO E CUSTOS PRINCIPAIS
    # ================================================================
    st.header("PASSO 5: Forma de Pagamento e Cálculo de Custos Principais")

    forma_pagamento = st.radio(
        "5.1 Forma de Pagamento:",
        ["À Vista", "Financiamento Caixa", "Parcelamento Judicial (CPC 895)"],
        help="Se judicial: CPC 895 (25% entrada + 30 parcelas). Extrajudicial: Pode haver financiamento bancário."
    )

    st.write("5.2 **Valor de arrematação (lance)** estimado:")
    valor_lance = st.number_input(
        "Informe o valor do lance (R$):",
        min_value=0.0, step=10000.0, format="%.2f",
        help="Quanto você imagina que oferecerá pelo imóvel no leilão?"
    )

    st.write("5.3 **Comissão do leiloeiro** (geralmente 5% do lance):")
    comissao_leiloeiro = valor_lance * 0.05

    st.write("5.4 **ITBI** (2% a 3% em média):")
    perc_itbi = st.slider(
        "Percentual de ITBI (%)", 
        1.0, 5.0, 2.5, 0.5,
        help="Ajuste conforme a cidade. Ex.: 2,5%."
    )
    itbi = valor_lance * (perc_itbi / 100.0)

    st.write("5.5 **Registro em Cartório** (1% a 1,5%):")
    perc_registro = st.slider(
        "Percentual de registro (%)", 
        0.5, 2.0, 1.2, 0.1,
        help="Custo do registro da transferência no Cartório de Imóveis."
    )
    registro_cartorio = valor_lance * (perc_registro / 100.0)

    st.write("5.6 **Dívidas passadas** (IPTU, condomínio, etc.):")
    debitos_passados = st.number_input(
        "Valor estimado (R$):",
        min_value=0.0, step=1000.0, format="%.2f",
        help="Verifique se o edital ou o banco cobre esses débitos."
    )

    st.write("5.7 Imóvel Ocupado? Acordo amigável para saída?")
    ocupado = st.radio(
        "O imóvel está ocupado?",
        ["Não", "Sim"],
        help="Se sim, verifique se a pessoa topa sair voluntariamente em troca de compensação."
    )
    valor_acordo = 0.0
    if ocupado == "Sim":
        acordo_amigavel = st.radio(
            "Há acordo amigável?",
            ["Sim", "Não"],
            help="Caso seja Não, avalie se você quer encarar ação de despejo."
        )
        if acordo_amigavel == "Sim":
            valor_acordo = st.number_input(
                "Valor de compensação (R$)",
                min_value=0.0, step=1000.0, format="%.2f",
                help="Ex.: um auxílio mudança para facilitar a desocupação amigável."
            )

    # Soma parcial
    custo_aquisicao_bruto = valor_lance + comissao_leiloeiro + itbi + registro_cartorio + debitos_passados + valor_acordo

    # ================================================================
    # PASSO 6: PAGAMENTOS E ETAPAS PÓS-ARREMATE
    # ================================================================
    st.header("PASSO 6: Pagamentos e Etapas Pós-Arremate")

    st.write("""
    **6.1 Se você for o vencedor** do leilão:
    - **Deposite** o valor (à vista, ou entrada + parcelas) no prazo estipulado.
    - Pague a **comissão do leiloeiro** (normalmente 5%).
    """)

    st.write("""
    **6.2 Solicite o documento**: 
    - Se for **Leilão Judicial**: Auto de Arrematação e posterior Carta de Arrematação.
    - Se for **Leilão Extrajudicial**: Contrato de Compra e Venda ou Escritura fornecida pelo banco.
    """)

    st.write("""
    **6.3 Pague o **ITBI** na Prefeitura e leve o comprovante para registrar a transferência 
    no Cartório de Registro de Imóveis.
    """)

    st.write("""
    **6.4 Faça o **Registro** da Carta/Escritura** em Cartório de Imóveis. Sem registro, você 
    não é oficialmente o dono.
    """)

    # ================================================================
    # PASSO 7: PLANEJAR REFORMA E PREPARAR PARA REVENDER (SE INVESTIMENTO)
    # ================================================================
    st.header("PASSO 7: Reforma e Revenda (se for o caso)")

    st.write("""
    Se o objetivo for **revender** ou **alugar**, planeje as **melhorias** que realmente gerem 
    valorização:
    - Estrutura (telhado, laje, elétrica, hidráulica)
    - Pintura, pisos, revestimentos
    - Banheiros e cozinha (modernizar)
    - Se for casa, fachada e jardim
    """)

    custo_reforma = st.number_input(
        "Custo previsto da reforma (R$):",
        min_value=0.0, step=1000.0, format="%.2f",
        help="Valor estimado para materiais + mão de obra."
    )

    # ================================================================
    # PASSO 8: RESUMO FINAL (GERAR RELATÓRIO)
    # ================================================================
    st.header("PASSO 8: Gerar Resumo Final")

    # Cálculo final
    custo_total = custo_aquisicao_bruto + custo_reforma

    # Se financiamento, calcular entrada e saldo
    valor_entrada = 0.0
    valor_financiado = 0.0
    if forma_pagamento == "Financiamento Caixa":
        # Exemplo simples: supondo entrada sobre o lance
        perc_entrada = st.slider(
            "Percentual de entrada (se Financiamento) (%)",
            5.0, 90.0, 25.0, 5.0,
            help="Ex.: 25% do valor do lance."
        )
        valor_entrada = valor_lance * (perc_entrada / 100.0)
        valor_financiado = max(valor_lance - valor_entrada, 0.0)

    # Botão para exibir relatório
    if st.button("Gerar Relatório Completo"):
        st.subheader("RELATÓRIO FINAL DO CHECKLIST")

        # Função de formatação BRL
        f_br = format_brl

        st.write(f"**Data:** {data_atual}")
        if nome_comprador:
            st.write(f"**Comprador:** {nome_comprador}")

        st.markdown("---")
        st.write("### Passo 1: Objetivos e Habilitação")
        st.write(f"- Objetivo principal: {objetivo}")
        st.write(f"- Habilitação para financiamento: {'Sim' if financiamento_pre else 'Não'}")
        st.write(f"- Orçamento máximo total: R$ {f_br(valor_orcamento_max)}")

        st.write("### Passo 2: Imóvel e Mercado")
        st.write(f"- Local (Cidade/Bairro): {local_imovel}")
        st.write(f"- Tipo de Imóvel: {tipo_imovel}")
        st.write(f"- Visitou o imóvel? {'Sim' if visitou else 'Não'}")
        st.write(f"- Conversou com corretores? {'Sim' if conversou_corretores else 'Não'}")
        st.write(f"- Valor de mercado estimado: R$ {f_br(valor_mercado)}")

        st.write("### Passo 3: Documentos e Edital")
        st.write(f"- Tipo de Leilão: {tipo_leilao}")
        st.write(f"- Edital lido? {'Sim' if edital_lido else 'Não'}")
        st.write(f"- Matrícula verificada? {'Sim' if matricula_conf else 'Não'}")
        if tipo_leilao == "Extrajudicial":
            st.write(f"- Antigo dono notificado corretamente? {('Sim' if notificacao_ok == 'Sim' else 'Não')}")

        st.write("### Passo 4: Cadastro e Participação")
        st.write(f"- Cadastro no site do leiloeiro feito? {'Sim' if cadastro_feito else 'Não'}")

        st.write("### Passo 5: Forma de Pagamento e Custos")
        st.write(f"- Forma de pagamento: {forma_pagamento}")
        if forma_pagamento == "Financiamento Caixa":
            st.write(f"  - Percentual de entrada: {perc_entrada}%")
            st.write(f"  - Valor de entrada (aprox): R$ {f_br(valor_entrada)}")
            st.write(f"  - Valor financiado (aprox): R$ {f_br(valor_financiado)}")

        st.write(f"- Lance (arrematação): R$ {f_br(valor_lance)}")
        st.write(f"- Comissão leiloeiro (5%): R$ {f_br(comissao_leiloeiro)}")
        st.write(f"- ITBI ({perc_itbi}%): R$ {f_br(itbi)}")
        st.write(f"- Registro em Cartório ({perc_registro}%): R$ {f_br(registro_cartorio)}")
        st.write(f"- Dívidas passadas: R$ {f_br(debitos_passados)}")

        if ocupado == "Sim":
            st.write("**Ocupado**: Sim")
            st.write(f"  - Valor de acordo (se amigável): R$ {f_br(valor_acordo)}")
        else:
            st.write("**Ocupado**: Não")

        aquisicao_formatada = f_br(valor_lance + comissao_leiloeiro + itbi + registro_cartorio + debitos_passados + valor_acordo)
        st.write(f"**Subtotal de Aquisição**: R$ {aquisicao_formatada}")

        st.write("### Passo 6: Pagamentos Pós-Arremate")
        st.write("Cheque prazos no edital, pague lance e comissão, faça ITBI e registre o imóvel.")

        st.write("### Passo 7: Reforma e Revenda")
        st.write(f"- Custo de reforma estimado: R$ {f_br(custo_reforma)}")

        total_formatado = f_br(custo_total)
        st.write(f"**Total Geral (Compra + Reforma)**: R$ {total_formatado}")

        st.success("Checklist finalizado com sucesso! Guarde este relatório para referência.")

if __name__ == "__main__":
    main()
