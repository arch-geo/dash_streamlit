import streamlit as st


with st.sidebar:
    st.title('O que é IMC?')
    #st.header("O que é IMC?")
    st.write("O Índice de Massa Corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal.")
    st.write("O IMC é determinado pela divisão da massa do indivíduo em quilogramas pelo quadrado de sua altura em metros.")


st.title('Calculadora de IMC')

peso = st.number_input('Peso (kg)', min_value=40, max_value=150, value=60)
altura = st.number_input('Altura (cm)', min_value=140, max_value=220, value = 170)

if st.button('Calcular IMC'):
    imc = peso / ((altura/100)**2)
    IMC_IDEAL = 21.7
    imc_delta = imc - IMC_IDEAL

    if imc < 18.5:
        resultado = {
            "classificacao": "Abaixo do peso",
            "delta_imc": imc_delta,
            "delta_peso": peso - IMC_IDEAL * ((altura/100)**2) 
        }

    elif imc < 25:
        resultado = {
            "classificacao": "Peso normal",
            "delta_imc": imc_delta,
            "delta_peso": peso - IMC_IDEAL * ((altura/100)**2) 
        }
    
    elif imc < 30:
        resultado = {
            "classificacao": "Sobrepeso",
            "delta_imc": imc_delta,
            "delta_peso": peso - IMC_IDEAL * ((altura/100)**2) 
        }

    elif imc < 40:
        resultado = {
            "classificacao": "Obesidade",
            "delta_imc": imc_delta,
            "delta_peso": peso - IMC_IDEAL * ((altura/100)**2) 
        }
    else:
        resultado = {
            "classificacao": "Obesidade mórbida",
            "delta_imc": imc_delta,
            "delta_peso": peso - IMC_IDEAL * ((altura/100)**2) 
        }

    col1, col2 = st.columns(2)
    col1.metric("IMC Classificado", resultado["classificacao"], round(resultado["delta_peso"],2), delta_color="inverse")
    col2.metric("IMC Calculado", round(imc,2), round(resultado["delta_imc"],2), delta_color="inverse")
    #col3.metric("IMC Ideal", round(IMC_IDEAL,2), delta_color="off")

    st.divider()

#st.image(r"https://www.saudebemestar.pt/media/89347/obesidade.jpg", width=600, caption="IMC")
