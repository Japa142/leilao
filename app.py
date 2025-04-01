import streamlit as st
import datetime

def main():
    st.title("Checklist de Compra de Imóveis em Leilão (GOIÁS)")
    st.write("""
    Este aplicativo ajuda você a seguir um passo a passo para avaliar e comprar imóveis em leilão 
    (judicial/extrajudicial), com possibilidade de financiamento pela Caixa.
    """)

    # Seção 1: Informações pessoais e do leilão
    st.header("1. Informações Básicas")
    nome_comprador = st.text_input("Nome do comprador (Pessoa Física)", "")
    data_hoje = datetime.date.today().strftime("%d/%m/%Y")
    st.write(f"Data de hoje: {data_hoje}")

    st.subheader("Objetivo e Orçamento")
    objetivo = st.selectbox("Qual o seu objetivo principal?", 
                            ["(Escolha)", "Moradia Própria", "Investimento (revenda/locação)", "Outros"])
    valor_maximo = st.number_input("Valor máximo que pretende investir (R$)", min_value=0.0, step=10000.0)

    # Seção 2: Dados do imóvel
    st.header("2. Dados do Imóvel")
    local_imovel = st.text_input("Cidade/Bairro do imóvel em Goiás", "")
    tipo_imovel = st.radio("Tipo de imóvel?", ["Casa", "Apartamento"])

    # Seção 3: Tipo de Leilão
    st.header("3. Informações do Leilão")
    tipo_leilao = st.radio("O leilão é Judicial ou Extrajudicial?", ["Judicial", "Extrajudicial"])
    financiamento = st.radio("Pretende financiar pela Caixa?", ["Sim", "Não"])

    # Seção 4: Ocupação do Imóvel
    st.header("4. Ocupação do Imóvel")
    ocupado = st.radio("O imóvel está ocupado?", ["Sim", "Não"])
    valor_acordo = 0.0
    acordo = "Não se aplica"
    if ocupado == "Sim":
        acordo = st.radio("Há possibilidade de acordo amigável para desocupação?", ["Sim", "Não"])
        if acordo == "Sim":
            valor_acordo = st.number_input("Valor para compensação financeira (auxílio para mudança, etc.)", 
                                           min_value=0.0, step=1000.0)

    # Seção 5: Documentação
    st.header("5. Documentação e Verificações")
    matricula_ok = st.checkbox("Verificou a matrícula atualizada (Certidão de inteiro teor)?")
    edital_ok = st.checkbox("Leu atentamente o edital do leilão?")
    debitos_ok = st.checkbox("Checou débitos de IPTU e condomínio?")
    visitou_imovel = st.checkbox("Visitou o imóvel presencialmente?")

    valor_mercado = st.number_input("Estimativa de valor de mercado do imóvel (R$)", min_value=0.0, step=10000.0)

    # Botão para gerar resumo
    if st.button("Gerar Resumo do Checklist"):
        st.subheader("Resumo do Checklist")
        st.write(f"**Data:** {data_hoje}")
        st.write(f"**Nome do comprador:** {nome_comprador if nome_comprador else 'Não informado'}")

        st.write("---")
        st.write(f"**Objetivo:** {objetivo if objetivo != '(Escolha)' else 'Não informado'}")
        st.write(f"**Valor máximo definido:** R$ {valor_maximo:,.2f}")

        st.write(f"**Local do imóvel (GO):** {local_imovel if local_imovel else 'Não informado'}")
        st.write(f"**Tipo de imóvel:** {tipo_imovel}")
        
        st.write(f"**Leilão:** {tipo_leilao}")
        st.write(f"**Financiamento Caixa:** {financiamento}")

        st.write(f"**Imóvel ocupado?** {ocupado}")
        if ocupado == "Sim":
            if acordo == "Sim":
                st.write(f"  - Acordo amigável: Sim, valor previsto de R$ {valor_acordo:,.2f}")
            else:
                st.write("  - [ALERTA] O ocupante não pretende sair amigavelmente.")
        
        st.write("---")
        st.write(f"**Matrícula verificada:** {'Sim' if matricula_ok else 'Não'}")
        st.write(f"**Edital lido:** {'Sim' if edital_ok else 'Não'}")
        st.write(f"**Débitos IPTU/condomínio verificados:** {'Sim' if debitos_ok else 'Não'}")
        st.write(f"**Visita presencial:** {'Sim' if visitou_imovel else 'Não'}")
        st.write(f"**Valor de mercado estimado:** R$ {valor_mercado:,.2f}")

        st.success("Checklist gerado com sucesso! Faça print ou salve as informações para seu registro.")

if __name__ == "__main__":
    main()
