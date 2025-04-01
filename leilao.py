import streamlit as st
import datetime

# ---------------------------------------------------------------------------
# Função para formatar valores em estilo brasileiro, ex: 120.000,00
# ---------------------------------------------------------------------------
def format_brl(value: float) -> str:
    """
    Formata valor float no estilo brasileiro: 1.234.567,89
    """
    if value is None:
        return ""
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def main():
    # -------------------------------------------------------------------------------------
    # CONFIGURAÇÃO INICIAL DA PÁGINA
    # -------------------------------------------------------------------------------------
    st.set_page_config(page_title="Checklist Ultra Completo - Leilão de Imóveis", layout="wide")
    st.title("Checklist Ultra Completo (Passo a Passo) - Compra de Imóveis em Leilão (GO)")

    st.write("""
    Este aplicativo contém um **passo a passo extremamente detalhado** para ajudar você a comprar 
    um imóvel em leilão (judicial ou extrajudicial) no estado de Goiás, **sem perder nenhum cuidado**.  
    Inclui orientações sobre **visita, documentação, notificação do antigo dono, uso de FGTS, 
    financiamento Caixa, verificação de dívidas, ocupação**, reforma e revenda.  
    Use-o como um **roteiro** para **não esquecer** nenhuma etapa crucial.
    """)

    # -------------------------------------------------------------------------------------
    # DADOS INICIAIS (BARRA LATERAL)
    # -------------------------------------------------------------------------------------
    data_hoje = datetime.date.today().strftime("%d/%m/%Y")
    st.sidebar.subheader("Dados Iniciais")
    nome_comprador = st.sidebar.text_input(
        "Seu nome (Pessoa Física):",
        help="Escreva seu nome completo ou como deseja ser identificado no relatório."
    )
    data_atual = st.sidebar.text_input("Data:", data_hoje)

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Sumário das Etapas:")
    st.sidebar.markdown("1. Definição de Objetivos e Orçamento")
    st.sidebar.markdown("2. Pesquisa e Análise de Mercado (visita, corretores)")
    st.sidebar.markdown("3. Verificação Documental (matrícula, edital, notificações)")
    st.sidebar.markdown("4. Ocupação do Imóvel (desocupado, acordo, etc.)")
    st.sidebar.markdown("5. Cadastro no Leiloeiro e Participação")
    st.sidebar.markdown("6. Forma de Pagamento e Cálculos de Custos")
    st.sidebar.markdown("7. Checagens Pós-Arremate (ITBI, registro, etc.)")
    st.sidebar.markdown("8. Reforma e Revenda")
    st.sidebar.markdown("9. Resumo Final")
    st.sidebar.markdown("10. Honorários, Seguros e Verificações Avançadas")
    st.sidebar.markdown("11. Documentos Complementares e Conclusão")
    st.sidebar.markdown("12. Checklist Detalhado (Antes, Durante, Depois)")
    st.sidebar.markdown("13. Diferenças e Cuidados: Judicial vs Extrajudicial")
    st.sidebar.markdown("14. Referências Úteis e Fontes de Consulta")

    st.write(f"**Data atual:** {data_atual}")
    if nome_comprador:
        st.write(f"**Nome do comprador:** {nome_comprador}")
    else:
        st.write("*Preencha o nome na barra lateral para personalizar.*")

    st.markdown("---")

    # ================================================================================
    # PASSO 1: DEFINIÇÃO DE OBJETIVOS E ORÇAMENTO
    # ================================================================================
    st.header("PASSO 1: Definição de Objetivos e Orçamento")

    st.write("""
    **1.1 - Objetivo da Compra**  
    Defina se a aquisição é para **moradia própria**, para **investir/revender** ou 
    para **alugar**. Isso influencia suas decisões (tipo de imóvel, valor de reforma, etc.).
    """)

    objetivo = st.selectbox(
        "Qual seu principal objetivo?",
        ["(Selecione)", "Moradia Própria", "Investimento (Revenda)", "Investimento (Locação)", "Outros"],
        help="Escolha a categoria que mais se aproxima do seu propósito."
    )

    st.write("""
    **1.2 - Orçamento Total**  
    Calcule quanto dinheiro, ao todo, você está disposto a aplicar (incluindo **lance, comissão, 
    ITBI, registro, eventuais dívidas, reforma**, etc.).
    """)

    valor_orcamento_max = st.number_input(
        "Orçamento máximo global (R$)",
        min_value=0.0, step=10000.0, format="%.2f",
        help="Inclua aqui TUDO que você pode gastar, não apenas o lance."
    )

    st.write("""
    **1.3 - Verificação de Financiamento (se houver)**  
    Se pretende financiar (ex.: Caixa), confira previamente seu **score**, documentos e se 
    **o nome no qual será financiado** atende aos requisitos (FGTS, tempo de trabalho, 
    limite de crédito, etc.).
    """)

    verificou_financiamento = st.checkbox(
        "Consultei a instituição financeira / Caixa para saber se tenho crédito/condições de financiamento?",
        help="Por exemplo, uma pré-aprovação de crédito, verificação de FGTS disponível, etc."
    )

    # ================================================================================
    # PASSO 2: PESQUISA E ANÁLISE DE MERCADO
    # ================================================================================
    st.header("PASSO 2: Pesquisa e Análise de Mercado (Visita, Corretores, etc.)")

    st.write("""
    **2.1 - Localização e Tipo de Imóvel**  
    Decida em qual região de Goiás (cidade/bairro) deseja comprar, e qual tipo (casa, apê).
    """)

    local_imovel = st.text_input(
        "Cidade/Bairro do imóvel (GO)",
        help="Ex.: Goiânia, setor, bairro, etc."
    )
    tipo_imovel = st.radio(
        "Tipo de imóvel:",
        ["Casa", "Apartamento", "Lote/Terreno", "Outros"],
        help="Selecione o tipo principal."
    )

    st.write("""
    **2.2 - Visita ao imóvel**  
    Sempre que possível, visite para avaliar **estado de conservação**, **vizinhança**, 
    **possíveis problemas** (rachaduras, infiltrações), etc.
    """)

    visitou = st.checkbox(
        "Realizei (ou vou realizar) a visita in loco?",
        help="Converse com vizinhos, síndico, porteiro para saber se há pendências ou problemas."
    )

    st.write("""
    **2.3 - Conversar com Corretores / Pesquisa de Mercado**  
    Fale com **corretores da região** e consulte sites (OLX, VivaReal, Imovelweb) para 
    comparar valores. Isso evita pagar acima do **valor de mercado**.
    """)

    conversou_corretores = st.checkbox(
        "Conversei com corretores e/ou fiz pesquisa online de valores na região?",
        help="Isso ajuda a comparar com o lance mínimo do leilão."
    )

    valor_mercado = st.number_input(
        "Valor de mercado estimado (R$)",
        min_value=0.0, step=10000.0, format="%.2f",
        help="Coloque aqui a média de preço que você acredita ser justo na região."
    )

    st.write("""
    **2.4 - Verificação de ampliações não averbadas**  
    Consulte, por exemplo, se a casa teve puxadinho ou área construída não registrada. 
    Isso pode gerar custos de regularização no futuro.
    """)

    verificou_averbacoes = st.checkbox(
        "Verifiquei se há construções não averbadas (o que pode exigir regularização)?",
        help="Pergunte a vizinhos, verifique a matrícula, planta na prefeitura, etc."
    )

    # ================================================================================
    # PASSO 3: VERIFICAÇÃO DOCUMENTAL (MATRÍCULA, EDITAL, NOTIFICAÇÕES)
    # ================================================================================
    st.header("PASSO 3: Verificação Documental (Matrícula, Edital, Notificações)")

    st.write("""
    **3.1 - Tipo de Leilão**  
    - **Judicial**: Acontece por determinação do juiz, com base no CPC (art. 879+).  
    - **Extrajudicial**: Normalmente alienação fiduciária (Lei 9.514/97), conduzida por bancos.  
    """)

    tipo_leilao = st.radio(
        "Tipo de leilão:",
        ["Judicial", "Extrajudicial"],
        help="Escolha conforme o edital - extrajudicial é tipicamente leilão de banco por inadimplência."
    )

    st.write("""
    **3.2 - Edital do Leilão**  
    Leia com extrema atenção:
    - Valor mínimo, datas, comissão, dívidas incluídas ou não.
    - Condições de pagamento (à vista, parcelado, financiamento).
    - Responsabilidade de desocupação.
    """)

    edital_lido = st.checkbox(
        "Li e compreendi o edital do leilão?",
        help="Verifique todas as cláusulas antes de dar qualquer lance."
    )

    st.write("""
    **3.3 - Matrícula do Imóvel**  
    Solicite a **certidão de inteiro teor** no Cartório de Registro de Imóveis. Verifique:
    - Proprietário atual
    - Penhoras, usufrutos, hipotecas
    - Consolidação (no caso de extrajudicial)
    - Averbações de penhora, execuções
    """)

    matricula_conf = st.checkbox(
        "Verifiquei a matrícula atualizada e vi se há ônus?",
        help="Documento essencial para avaliar pendências."
    )

    st.write("""
    **3.4 - Notificações do Antigo Dono** (Leilão Extrajudicial)  
    Se for extrajudicial, confirmar se houve notificação adequada do devedor (Lei 9.514/97).
    Falhas podem anular o leilão.
    """)

    notificacao_ok = "Não se aplica (Leilão Judicial)"
    if tipo_leilao == "Extrajudicial":
        check_notif = st.checkbox(
            "Confirmado que o antigo dono foi notificado corretamente (conforme matrícula)?",
            help="Verifique se consta no registro a intimação formal do devedor."
        )
        notificacao_ok = "Sim" if check_notif else "Não"

    st.write("""
    **3.5 - Verificar processos judiciais correlatos**  
    Pesquise se há **outras ações** (ex.: usucapião, falência, inventário) no nome do proprietário. 
    Acesse o site do TJGO ou fale com um advogado.
    """)

    verificou_processos = st.checkbox(
        "Consultei processos no TJGO em nome do devedor/proprietário?",
        help="Isso evita surpresas como outra penhora, etc."
    )

    # ================================================================================
    # PASSO 4: OCUPAÇÃO DO IMÓVEL
    # ================================================================================
    st.header("PASSO 4: Ocupação do Imóvel (Desocupado x Ocupado)")

    st.write("""
    **4.1 - O imóvel está desocupado ou ocupado?**  
    - **Desocupado**: Posse mais fácil.
    - **Ocupado**: Pode ser ex-proprietário, inquilino ou até invasor.
    """)

    ocupado = st.radio(
        "Situação de ocupação:",
        ["Desocupado", "Ocupado"],
        help="Se ocupado, analise a possibilidade de acordo amigável ou ação judicial."
    )

    acordo_amigavel = "Não se aplica"
    valor_acordo = 0.0
    if ocupado == "Ocupado":
        st.write("""
        **4.2 - Acordo Amigável**  
        Tente negociar (ex.: pagar ajuda mudança) se o ocupante aceitar sair sem briga.
        """)
        acordo_amigavel = st.radio(
            "Haverá acordo amigável?",
            ["Sim", "Não"],
            help="Se não, avalie se deseja encarar ação de despejo ou desistir do leilão."
        )
        if acordo_amigavel == "Sim":
            valor_acordo = st.number_input(
                "Valor de compensação (R$):",
                min_value=0.0, step=1000.0, format="%.2f",
                help="Ex.: 5.000 para mudança."
            )

    st.write("""
    **4.3 - Contrato de Locação Vigente?**  
    Se houver inquilino com contrato em vigor, a Lei do Inquilinato permite ao novo dono 
    rescindir (denúncia) em 90 dias.
    """)

    verificou_locacao = st.checkbox(
        "Verifiquei se há contrato de locação em vigor?",
        help="Pode ser que o inquilino tenha que ficar por 90 dias pagando aluguel ao novo dono."
    )

    # ================================================================================
    # PASSO 5: CADASTRO NO LEILOEIRO E PARTICIPAÇÃO
    # ================================================================================
    st.header("PASSO 5: Cadastro no Leiloeiro e Participação no Leilão")

    st.write("""
    **5.1 - Cadastro no Site / Habilitação**  
    - Preencher dados (RG, CPF, comprovante de residência).
    - Alguns leilões pedem caução (sinal) para se habilitar.
    """)

    cadastro_feito = st.checkbox(
        "Fiz ou vou fazer o cadastro no site do leiloeiro / portal do tribunal?",
        help="Sem cadastro/habilitação, você não pode dar lances, principalmente nos online."
    )

    st.write("""
    **5.2 - Data e Hora do Leilão**  
    - Anotar no calendário.
    - Conferir se houve adiamento/suspensão (ex.: pagamento de dívida de última hora).
    """)

    verifica_data_leilao = st.checkbox(
        "Verifiquei a data/hora e me programei para estar presente ou online?",
        help="É comum haver mudança de data se o devedor paga a dívida."
    )

    # ================================================================================
    # PASSO 6: FORMA DE PAGAMENTO E CÁLCULOS DE CUSTOS
    # ================================================================================
    st.header("PASSO 6: Forma de Pagamento e Cálculos de Custos Principais")

    st.write("""
    **6.1 - Valor de Arrematação (Lance)**  
    Informe abaixo quanto você imagina que o imóvel deve ser arrematado no leilão.
    """)

    valor_lance = st.number_input(
        "Valor estimado de arrematação (R$):",
        min_value=0.0, step=10000.0, format="%.2f"
    )

    st.write("""
    **6.2 - Forma de Pagamento**  
    - **À Vista**  
    - **Financiamento Caixa** (extrajudicial, ou se o leilão permitir)  
    - **Parcelamento Judicial** (CPC art. 895: 25% + até 30 parcelas)
    """)

    forma_pagamento = st.radio(
        "Escolha a forma de pagamento:",
        ["À Vista", "Financiamento Caixa", "Parcelamento Judicial (CPC 895)"],
        help="Verifique no edital se permitem financiamento ou parcelamento."
    )

    # Caso financiamento, perguntar sobre a entrada
    perc_entrada = 0.0
    valor_entrada = 0.0
    valor_financiado = 0.0
    if forma_pagamento == "Financiamento Caixa":
        st.write("""
        **Entrada (%)**  
        Geralmente 20% a 30% do valor. O resto vira financiamento. Pode usar FGTS se o imóvel 
        e o comprador atenderem às regras (ex.: uso para moradia própria).
        """)
        perc_entrada = st.slider(
            "Percentual de entrada (Financiamento) (%)",
            5.0, 90.0, 25.0, 5.0,
            help="Selecione a % de entrada. Ex.: 25% do lance."
        )
        valor_entrada = valor_lance * (perc_entrada / 100.0)
        valor_financiado = max(valor_lance - valor_entrada, 0.0)

    st.write("""
    **6.3 - Comissão do Leiloeiro (geralmente 5%)**
    """)
    comissao_leiloeiro = valor_lance * 0.05

    st.write("""
    **6.4 - ITBI** (em média 2% a 3% no município; alguns podem variar)
    """)
    perc_itbi = st.slider(
        "Taxa de ITBI (%)",
        1.0, 5.0, 2.5, 0.5,
        help="Altere conforme a sua prefeitura, ex.: 2,5%."
    )
    itbi = valor_lance * (perc_itbi / 100.0)

    st.write("""
    **6.5 - Registro em Cartório** (1% a 1,5% do valor)
    """)
    perc_registro = st.slider(
        "Porcentagem de registro em cartório (%)",
        0.5, 2.0, 1.2, 0.1,
        help="Ex.: 1,2% do valor do imóvel."
    )
    registro_cartorio = valor_lance * (perc_registro / 100.0)

    st.write("""
    **6.6 - Dívidas passadas** (IPTU, condomínio, água, etc.)
    """)
    debitos_passados = st.number_input(
        "Valor estimado de dívidas (R$)",
        min_value=0.0, step=1000.0, format="%.2f",
        help="Nem sempre o banco/leiloeiro paga essas dívidas. Verifique no edital."
    )

    # Usamos valor_acordo definido acima (PASSO 4)
    st.write("""
    **6.7 - Somatório parcial** (Aquisição)
    """)
    custo_aquisicao_bruto = (valor_lance + comissao_leiloeiro + itbi
                             + registro_cartorio + debitos_passados + valor_acordo)

    # ================================================================================
    # PASSO 7: CHECAGENS PÓS-ARREMATE (PAGAMENTOS, ITBI, REGISTRO)
    # ================================================================================

    st.header("PASSO 7: Checagens Pós-Arremate (Pagamento, ITBI, Registro, etc.)")

    st.write("""  
    **7.1 - Se você der o lance vencedor**:  
     1) Deposite o valor (ou a entrada) no prazo do edital (24h, 48h, etc.)  
     2) Pague a comissão do leiloeiro no prazo estabelecido  
     3) Se judicial, aguarde a homologação do juiz e emissão do Auto/Carta de Arrematação  
     4) Se extrajudicial (banco), assine o contrato de compra e venda ou escritura  

    **Ações práticas para cada etapa:**  
    - Verifique a conta bancária informada para o depósito do lance.  
    - Envie o comprovante de pagamento ao leiloeiro (ou junte nos autos, se judicial).  
    - Acompanhe o andamento do processo (judicial) ou contato com o banco (extrajudicial).  
    - Se financiamento, continue com a documentação (análise de crédito, assinatura de contrato).  
    """)

    depositou_valor = st.checkbox(
        "Depositei o valor/entrada no prazo (7.1.1)?",
        help="Confirme que realizou o depósito (à vista ou entrada do financiamento) dentro do prazo."
    )
    pagou_comissao = st.checkbox(
        "Paguei a comissão do leiloeiro (7.1.2)?",
        help="Normalmente 5% do lance, verifique prazo e conta específica do leiloeiro."
    )
    judicial_homologacao = st.checkbox(
        "No caso de leilão judicial, aguardei homologação e recebi a Carta de Arrematação (7.1.3)?",
        help="Marque se for judicial e já tiver cumprido essa etapa (aguardar juiz)."
    )
    extrajudicial_assinou = st.checkbox(
        "No caso de leilão extrajudicial (banco), assinei contrato ou escritura (7.1.4)?",
        help="Marque se for extrajudicial e tiver assinado com o banco/vendedor."
    )

    st.write("""  
    **7.2 - Pague o ITBI** na prefeitura para poder efetuar o registro.  
    Apresente o comprovante no cartório.

    Observações:  
    - Verifique a guia de recolhimento do ITBI na prefeitura.  
    - Após o pagamento, pegue o comprovante oficial para levar ao cartório.
    """)
    pagou_itbi = st.checkbox(
        "Já paguei o ITBI e tenho o comprovante (7.2)?",
        help="Sem esse comprovante, o cartório não efetua o registro no seu nome."
    )

    st.write("""  
    **7.3 - Registre** a carta ou escritura no Cartório de Registro de Imóveis para oficializar a propriedade.  

    Observações:  
    - Para judicial: use a Carta de Arrematação emitida pelo juiz.  
    - Para extrajudicial: use a escritura ou contrato fornecido pelo banco, levando em conta o pagamento do ITBI.  
    - Verifique se o cartório exige alguma certidão adicional ou guias pagas.
    """)
    registrou_imovel = st.checkbox(
        "Já efetuei o registro no Cartório de Imóveis (7.3)?",
        help="Somente após o registro você se torna oficialmente proprietário perante terceiros."
    )

    st.write("""  
    **7.4 - Se o imóvel estiver ocupado e não houver acordo**, inicie a ação de imissão na posse (judicial) 
    ou use o mandado (se for judicial).  

    Observações:  
    - Para leilão judicial, solicite o Mandado de Imissão na Posse após homologação.  
    - Para extrajudicial, precisará de uma ação autônoma de imissão na posse.
    """)
    acao_posse = st.checkbox(
        "Precisei (ou vou precisar) ingressar com ação de imissão na posse (7.4)?",
        help="Marque se houver ocupante resistente e você não obtiver posse amigável."
    )

    # ================================================================================
    # PASSO 8: PLANEJAMENTO DE REFORMA E REVENDA (SE INVESTIMENTO)
    # ================================================================================
    st.header("PASSO 8: Reforma e Revenda (se for investimento)")

    st.write("""
    **8.1 - Planeje a reforma**:
    - Itens estruturais (telhado, laje, infiltrações)
    - Elétrica, hidráulica
    - Revestimentos, piso, pintura
    - Fachada (se for casa)
    - Modernização de cozinha e banheiros
    """)

    custo_reforma = st.number_input(
        "Custo estimado da reforma (R$)",
        min_value=0.0, step=1000.0, format="%.2f",
        help="Baseie-se em orçamentos com profissionais confiáveis."
    )

    st.write("""
    **8.2 - Se a ideia é revender**:
    - Pesquise o preço de revenda pós-reforma.
    - Se possível, considere **retorno sobre investimento** (ROI).
    - Verifique o tempo para a reforma e legalização (se for necessário atualizar matrículas, projetos).
    """)

    # ================================================================================
    # PASSO 9: RESUMO FINAL (RELATÓRIO)
    # ================================================================================
    st.header("PASSO 9: Resumo Final e Geração de Relatório")

    investimento_total = custo_aquisicao_bruto + custo_reforma

    # ================================================================================
    # PASSO 10: HONORÁRIOS, SEGUROS, VERIFICAÇÕES AVANÇADAS
    # (NOVO - ADICIONADO SEM RETIRAR NADA DO SCRIPT)
    # ================================================================================
    st.header("PASSO 10: Honorários, Seguros e Verificações Avançadas")

    st.write("""
    **10.1 - Honorários Advocatícios** (se necessários):  
    - Caso contrate um advogado para acompanhamento do leilão, ocupação, ou 
      ações judiciais de imissão na posse, consulte o valor.  
    """)

    honorarios_adv = st.number_input(
        "Honorários advocatícios estimados (R$)",
        min_value=0.0, step=1000.0, format="%.2f",
        help="Se houver advogado para acompanhar todo o processo."
    )

    st.write("""
    **10.2 - Seguro do Imóvel**  
    - Se pretende reformar, é prudente contratar um **seguro residencial** para cobrir 
      possíveis danos (furto de materiais, sinistros) durante a obra.  
    - Também avalie um seguro após a reforma, se for alugar ou manter.  
    """)

    seguro_imovel = st.number_input(
        "Custo estimado de seguro (R$)",
        min_value=0.0, step=100.0, format="%.2f",
        help="Ex.: Seguro residencial básico, anual."
    )

    st.write("""
    **10.3 - Verificações Adicionais**  
    - Certidões pessoais do ex-proprietário (protesto, execuções) para evitar surpresas.  
    - Possíveis débitos de condomínio não declarados.  
    - Se for área rural (não é o caso aqui, mas vale lembrar) verificar CCIR, ITR.  
    """)

    custo_total_avancado = investimento_total + honorarios_adv + seguro_imovel

    # ================================================================================
    # PASSO 11: DOCUMENTOS COMPLEMENTARES E CONCLUSÃO
    # (NOVO - ADICIONADO SEM RETIRAR NADA DO SCRIPT)
    # ================================================================================
    st.header("PASSO 11: Documentos Complementares e Conclusão")

    st.write("""
    **11.1 - Guarde todos os documentos**:  
    - Edital, comprovantes de depósito do lance, comissão, ITBI.  
    - Matrícula atualizada pós-registro em seu nome.  
    - Contrato/Escritura (extrajudicial) ou Carta de Arrematação (judicial).  
    - Notas fiscais de material de construção (caso reforme).  
    """)

    st.write("""
    **11.2 - Finalização**  
    - Ao concluir a reforma (se houver), faça nova vistoria.  
    - Se for morar, transfira serviços (luz, água, IPTU) para seu nome.  
    - Se for vender/alugar, divulgue o imóvel com as características atualizadas (fotos, 
      documentação em dia).
    """)

    # ================================================================================
    # PASSO 12: CHECKLIST DETALHADO (ANTES, DURANTE E APÓS) - EXTRA EXPANDER
    # ================================================================================
    st.header("PASSO 12: Checklist Detalhado (Antes, Durante e Depois)")

    with st.expander("Ver texto completo do Passo a Passo (Antes do Leilão, Durante, Após)"):
        st.markdown("""
        ### Antes do Leilão (Preparação)

        - **Defina seu objetivo e orçamento**: Moradia ou investimento? Quanto pode pagar no total?  
        - **Pesquisa de mercado e plataformas confiáveis**: Consulte portais como Imóveis Caixa, TJGO, 
          leiloeiros registrados na JUCEG.  
        - **Selecione imóveis e avalie viabilidade**: Compare preço mínimo x valor de mercado, 
          potencial de retorno.  
        - **Inspeção in loco**: Verifique a construção, conservação, problemas estruturais.  
          Converse com vizinhos, síndico.  
        - **Verificar ocupação** (desocupado, amigável, hostil).  
        - **Análise da documentação** (Matrícula atualizada, penhoras, hipotecas, consolidação no 
          extrajudicial).  
        - **Leia atentamente o edital**: Valor mínimo, comissão, responsabilidades por dívidas, 
          forma de pagamento, etc.  
        - **Verifique débitos** (IPTU, condomínio, água, luz).  
        - **Analise viabilidade financeira completa** (lance + dívidas + reforma + taxas).  
        - **Consulta a processos judiciais** (nome do devedor, usucapião, falência).  
        - **Cadastre-se e habilite-se** (documentos, caução).  
        - **Planeje pagamento** (à vista, parcelamento CPC 895, financiamento Caixa).  
        - **Agende alertas** e fique atento a possíveis suspensões.

        ### Durante o Leilão (Lances e Arremate)

        - **Acompanhe pontualmente**: Presencial ou online, com login feito.  
        - **Tenha informações-chave à mão**: Valor máximo, condições do edital, débitos.  
        - **Faça lances com estratégia**, não ultrapasse seu limite, cuidado com “febre do leilão”.  
        - **Ofertas à vista x parceladas**: À vista tem preferência sobre valor igual parcelado 
          (judicial).  
        - **Seja o lance vencedor**: Anote o valor final, assine o auto de arrematação (ou 
          aguarde confirmação online).  
        - **Solicite orientações de pagamento ao leiloeiro** (prazo, conta bancária, TED).  
        - **Não perca os prazos** (24h, 48h).  
        - **Registro do auto de arrematação** (judicial) e aguarde homologação.  
        - **Prazo de impugnação** (judicial, ~10 dias). Em extrajudicial, não há homologação 
          pelo juiz, mas ex-proprietário pode mover ação anulatória.

        ### Após o Arremate (Pós-leilão e Posse)

        - **Guarde comprovantes** de pagamento e taxas.  
        - **Formalize a transferência**:
          - Judicial: Carta/Auto de Arrematação -> Registro de Imóveis.  
          - Extrajudicial: Escritura (à vista) ou Contrato de Financiamento, depois registre.  
        - **Pague ITBI** e apresente comprovante para registrar.  
        - **Posse do imóvel**:
          - Desocupado: troque fechaduras.  
          - Ocupado: Se acordo amigável, cumpra os termos. Caso contrário, ação de imissão na 
            posse ou mandado judicial.  
          - Inquilino: Lei do Inquilinato (90 dias).  
        - **Quite dívidas remanescentes** (IPTU, condomínio).  
        - **Remova ônus na matrícula** (ofícios judiciais ou documentos do banco).  
        - **Use FGTS ou finalize financiamento** se aplicável.  
        - **Providências extras**: seguro, documentar condição do imóvel, guardar todos os papéis.
        """)

    # ================================================================================
    # PASSO 13: DIFERENÇAS E CUIDADOS - EXTRA EXPANDER
    # ================================================================================
    st.header("PASSO 13: Diferenças e Cuidados - Leilão Judicial vs Extrajudicial")

    with st.expander("Clique para ver detalhes do Judicial x Extrajudicial"):
        st.markdown("""
        - **Origem**:
          - Judicial: Bem penhorado em processo de execução (cível, trabalhista, fiscal).  
          - Extrajudicial: Alienação fiduciária (Lei 9.514/97) ou execução privada por bancos.

        - **Legislação aplicada**:
          - Judicial: CPC (arts. 879-903), com supervisão do juiz.  
          - Extrajudicial: Lei 9.514/97, normas contratuais, leiloeiro público, sem ação judicial 
            (a princípio).

        - **Publicidades e intimações**:
          - Judicial: Citação do devedor, edital publicado em diário oficial.  
          - Extrajudicial: Notificação cartorária, edital em jornal de grande circulação.

        - **Primeira e segunda praça/leilão**:
          - Judicial: 1ª praça >= avaliação, 2ª >= 50% (ou mínimo estipulado).  
          - Extrajudicial: 1º leilão >= dívida ou valor de avaliação; 2º leilão pode ser menor.

        - **Pagamento e financiamento**:
          - Judicial: Parcelamento (CPC 895) é possível, mas não financiamento bancário direto.  
          - Extrajudicial: Bancos costumam oferecer financiamento (ex.: Caixa).

        - **Regularização de dívidas**:
          - Judicial: Normalmente as dívidas propter rem ficam para o arrematante, salvo se 
            o valor arrecadado for suficiente e o juiz destinar para quitar.  
          - Extrajudicial (bancos): Muitos pagam IPTU/condomínio em atraso até a data do leilão, 
            liberando o imóvel de débitos.

        - **Posse e desocupação**:
          - Judicial: Você obtém mandado de imissão na posse após a homologação, caso necessário.  
          - Extrajudicial: Se ocupado, precisa entrar com ação de imissão na posse na justiça 
            comum, pois não há ordem judicial direta do leilão.

        - **Conclusão do negócio**:
          - Judicial: Carta de arrematação substitui escritura pública, mas precisa registro.  
          - Extrajudicial: Escritura ou contrato do banco + registro no cartório.
        """)

    # ================================================================================
    # PASSO 14: REFERÊNCIAS ÚTEIS E FONTES DE CONSULTA
    # ================================================================================
    st.header("PASSO 14: Referências Úteis e Fontes de Consulta")

    with st.expander("Clique para ver Referências"):
        st.markdown("""
        - **Tribunal de Justiça de Goiás (TJGO)**:
          - Site oficial para leilões judiciais, consulta processual.
        - **Caixa Econômica Federal – Imóveis à Venda**:
          - [venda-imoveis.caixa.gov.br](https://venda-imoveis.caixa.gov.br)  
          - Filtros por cidade e modalidade (leilão, licitação, venda direta).
        - **Cartórios de Registro de Imóveis (Goiás)**:
          - Central Registradores de Imóveis (ONR) ou cartório local para certidões.
        - **Legislação básica**:
          - CPC (Lei 13.105/2015), arts. 879-903 (leilão judicial).
          - Lei 9.514/97 (alienação fiduciária).
          - Lei do Inquilinato (8.245/91, art. 8º).
        - **Materiais de apoio**:
          - Checklist de Arrematação D1Lance, artigos de especialistas, jurisprudência.
        """)

    # BOTÃO FINAL PARA EXIBIR O RELATÓRIO COMPLETO
    if st.button("Gerar Relatório Completo"):
        st.subheader("RELATÓRIO FINAL DO CHECKLIST - ULTRA COMPLETO")

        f_br = format_brl  # para formatar valores

        # Título e dados básicos
        st.write(f"**Data:** {data_atual}")
        if nome_comprador:
            st.write(f"**Nome do Comprador:** {nome_comprador}")

        st.markdown("---")
        st.write("### PASSO 1: Objetivos e Orçamento")
        st.write(f"- Objetivo: {objetivo}")
        st.write(f"- Orçamento Máximo: R$ {f_br(valor_orcamento_max)}")
        st.write(f"- Verificou Financiamento previamente? {'Sim' if verificou_financiamento else 'Não'}")

        st.write("### PASSO 2: Mercado e Visita")
        st.write(f"- Local (GO): {local_imovel}")
        st.write(f"- Tipo de Imóvel: {tipo_imovel}")
        st.write(f"- Visita In Loco? {'Sim' if visitou else 'Não'}")
        st.write(f"- Conversou com corretores/pesquisa online? {'Sim' if conversou_corretores else 'Não'}")
        st.write(f"- Valor de Mercado Estimado: R$ {f_br(valor_mercado)}")
        st.write(f"- Conferiu possíveis ampliações não averbadas? {'Sim' if verificou_averbacoes else 'Não'}")

        st.write("### PASSO 3: Documentos e Edital")
        st.write(f"- Tipo de Leilão: {tipo_leilao}")
        st.write(f"- Edital lido? {'Sim' if edital_lido else 'Não'}")
        st.write(f"- Matrícula verificada? {'Sim' if matricula_conf else 'Não'}")
        if tipo_leilao == "Extrajudicial":
            st.write(f"- Antigo dono notificado? {notificacao_ok}")
        st.write(f"- Pesquisou processos no TJGO? {'Sim' if verificou_processos else 'Não'}")

        st.write("### PASSO 4: Ocupação")
        st.write(f"- Ocupação do Imóvel: {ocupado}")
        if ocupado == "Ocupado":
            st.write(f"  - Acordo amigável? {acordo_amigavel}")
            if acordo_amigavel == "Sim":
                st.write(f"  - Valor de acordo: R$ {f_br(valor_acordo)}")
        st.write(f"- Contrato de locação verificado? {'Sim' if verificou_locacao else 'Não'}")

        st.write("### PASSO 5: Cadastro e Participação no Leilão")
        st.write(f"- Cadastro no leiloeiro feito? {'Sim' if cadastro_feito else 'Não'}")
        st.write(f"- Verificou data/hora do leilão? {'Sim' if verifica_data_leilao else 'Não'}")

        st.write("### PASSO 6: Forma de Pagamento e Cálculos")
        st.write(f"- Valor do Lance: R$ {f_br(valor_lance)}")
        st.write(f"- Forma de Pagamento: {forma_pagamento}")
        if forma_pagamento == "Financiamento Caixa":
            st.write(f"  - % de Entrada: {perc_entrada}%")
            st.write(f"  - Valor de Entrada (aprox.): R$ {f_br(valor_entrada)}")
            st.write(f"  - Valor Financiado (aprox.): R$ {f_br(valor_financiado)}")

        st.write(f"- Comissão do Leiloeiro (5%): R$ {f_br(comissao_leiloeiro)}")
        st.write(f"- ITBI ({perc_itbi}%): R$ {f_br(itbi)}")
        st.write(f"- Registro em Cartório ({perc_registro}%): R$ {f_br(registro_cartorio)}")
        st.write(f"- Dívidas Passadas (IPTU/condomínio): R$ {f_br(debitos_passados)}")

        if valor_acordo > 0:
            st.write(f"- Valor de Acordo Ocupante: R$ {f_br(valor_acordo)}")

        st.write(f"**Subtotal de Aquisição**: R$ {f_br(custo_aquisicao_bruto)}")

        # RESUMO DO PASSO 7
        st.write("### PASSO 7: Pós-Arremate - Checkpoints")
        st.write(f"- Depósito do valor no prazo? {'Sim' if depositou_valor else 'Não'}")
        st.write(f"- Pagamento da comissão do leiloeiro? {'Sim' if pagou_comissao else 'Não'}")
        st.write(f"- (Judicial) Homologação / Carta de Arrematação recebida? {'Sim' if judicial_homologacao else 'Não'}")
        st.write(f"- (Extrajudicial) Contrato/escritura com o banco? {'Sim' if extrajudicial_assinou else 'Não'}")
        st.write(f"- ITBI pago e comprovado? {'Sim' if pagou_itbi else 'Não'}")
        st.write(f"- Registro no Cartório de Imóveis efetuado? {'Sim' if registrou_imovel else 'Não'}")
        st.write(f"- Ação de imissão na posse iniciada (se necessário)? {'Sim' if acao_posse else 'Não'}")

        st.write("### PASSO 8: Reforma e Revenda")
        st.write(f"- Custo de Reforma: R$ {f_br(custo_reforma)}")
        total_formatado = f_br(investimento_total)
        st.write(f"**Investimento Total (Compra + Reforma)**: R$ {total_formatado}")

        # PASSO 10 - RELATÓRIO
        st.write("### PASSO 10: Honorários, Seguros e Verificações Avançadas")
        st.write(f"- Honorários advocatícios: R$ {f_br(honorarios_adv)}")
        st.write(f"- Seguro do Imóvel: R$ {f_br(seguro_imovel)}")

        total_geral_avancado = investimento_total + honorarios_adv + seguro_imovel
        st.write(f"**Total Geral (Compra + Reforma + Honorários + Seguro)**: R$ {f_br(total_geral_avancado)}")

        # PASSO 11 - RELATÓRIO
        st.write("### PASSO 11: Documentos Complementares e Conclusão")
        st.write("""
        - Guarde todos os comprovantes e documentos (edital, matrícula, recibos de pagamento).
        - Atualize cadastros de água, luz, IPTU, e eventualmente disponibilize o imóvel para venda/locação.
        """)

        st.success(f"""
        **Checklist concluído**!  
        Você finalizou todas as etapas do roteiro de compra de imóvel em leilão.  
        Caso precise de suporte jurídico, consulte um advogado especializado.  
        **Valor Final c/ Honorários e Seguro**: R$ {f_br(total_geral_avancado)}
        """)

# ---------------------------------------------------------------------------
# RODAR A APLICAÇÃO
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()
